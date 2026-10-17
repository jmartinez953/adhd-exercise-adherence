import csv
import json
import re
import pyexpat
from pathlib import Path

# ElementTree uses Expat, which does not open local files or network connections;
# Expat 2.7.2+ also limits entity expansion, enforced by check_expat().
import xml.etree.ElementTree as ET


COLUMNS = [
    "pmid",
    "title",
    "year",
    "journal",
    "abstract",
    "publication_types",
    "doi",
    "pmcid",
]


def check_expat(version=None):
    found = version or pyexpat.EXPAT_VERSION
    numbers = tuple(int(part) for part in re.match(r"expat_(\d+\.\d+\.\d+)", found).group(1).split("."))
    if numbers < (2, 7, 2):
        raise RuntimeError(f"Expat {found} is too old; minimum supported version is 2.7.2")


def _name(element):
    return element.tag.rsplit("}", 1)[-1]


def _text(element):
    return " ".join("".join(element.itertext()).split()) if element is not None else ""


def _row(article):
    if _name(article) == "PubmedBookArticle":
        document = article.find("BookDocument")
        book = document.find("Book") if document is not None else None
        title = document.find("ArticleTitle") if document is not None else None
        if title is None and book is not None:
            title = book.find("BookTitle")
        pub_date = book.find("PubDate") if book is not None else None
        pmid = document.find("PMID") if document is not None else None
        journal = None
        year = pub_date.find("Year") if pub_date is not None else None
        abstract_sections = (
            document.findall("Abstract/AbstractText") if document is not None else []
        )
        publication_types = (
            document.findall("PublicationType") if document is not None else []
        )
        article_id_list = article.find("PubmedBookData/ArticleIdList")
    else:
        citation = article.find("MedlineCitation")
        medline_article = citation.find("Article") if citation is not None else None
        pub_date = (
            medline_article.find("Journal/JournalIssue/PubDate")
            if medline_article is not None
            else None
        )
        pmid = citation.find("PMID") if citation is not None else None
        title = medline_article.find("ArticleTitle") if medline_article is not None else None
        journal = medline_article.find("Journal/Title") if medline_article is not None else None
        year = pub_date.find("Year") if pub_date is not None else None
        abstract_sections = (
            medline_article.findall("Abstract/AbstractText")
            if medline_article is not None
            else []
        )
        publication_types = (
            medline_article.findall("PublicationTypeList/PublicationType")
            if medline_article is not None
            else []
        )
        article_id_list = article.find("PubmedData/ArticleIdList")

    if year is None:
        medline_date = pub_date.find("MedlineDate") if pub_date is not None else None
        match = re.search(r"\b\d{4}\b", _text(medline_date))
        year_text = match.group(0) if match else ""
    else:
        year_text = _text(year)

    abstract_parts = []
    for section in abstract_sections:
        text = _text(section)
        label = section.attrib.get("Label", "").strip()
        abstract_parts.append(f"{label}: {text}" if label else text)

    ids = {}
    if article_id_list is not None:
        for child in article_id_list.findall("ArticleId"):
            ids[child.attrib.get("IdType", "").lower()] = _text(child)

    return {
        "pmid": _text(pmid),
        "title": _text(title),
        "year": year_text,
        "journal": _text(journal),
        "abstract": " ".join(abstract_parts),
        "publication_types": "; ".join(_text(child) for child in publication_types),
        "doi": ids.get("doi", ""),
        "pmcid": ids.get("pmc", ""),
    }


def parse_file(path):
    check_expat()
    root = ET.parse(path).getroot()
    articles = [
        element
        for element in root.iter()
        if _name(element) in {"PubmedArticle", "PubmedBookArticle"}
    ]
    return [_row(article) for article in articles]


def write_csv(rows, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def parse_harvest(raw_dir, manifest_path, csv_path):
    check_expat()
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    rows = []
    for path in sorted(Path(raw_dir).glob("batch-*.xml")):
        rows.extend(parse_file(path))

    expected = {str(pmid) for pmid in manifest["pmids"]}
    actual = {row["pmid"] for row in rows}
    if expected != actual:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ValueError(f"PMID mismatch; missing: {missing}; extra: {extra}")
    write_csv(rows, csv_path)
    return rows


def main():
    manifests = sorted(Path("data/manifests").glob("*.json"))
    if not manifests:
        raise FileNotFoundError("no manifest found in data/manifests")
    manifest_path = manifests[-1]
    date = manifest_path.stem
    csv_path = Path("data/candidates") / f"{date}.csv"
    rows = parse_harvest(Path("data/raw") / date, manifest_path, csv_path)
    print(f"{len(rows)} rows")
    print(csv_path)
    return rows


if __name__ == "__main__":
    main()
