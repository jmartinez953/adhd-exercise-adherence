import json
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


EUTILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
MIN_REQUEST_INTERVAL = 0.34


def read_query(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    markers = [number for number, line in enumerate(lines) if line.strip() == "~~~"]
    if len(markers) != 2 or markers[1] != markers[0] + 2:
        raise ValueError("expected exactly one query line between two ~~~ lines")
    query = lines[markers[0] + 1].strip()
    if not query:
        raise ValueError("expected exactly one non-empty query line")
    return query


def get_email():
    try:
        return os.environ["NCBI_EMAIL"]
    except KeyError as error:
        raise RuntimeError("NCBI_EMAIL is not set; set it to your email address") from error


def fetch(url, params):
    request_params = dict(params)
    request_params["tool"] = "adhd-exercise-adherence"
    request_params.setdefault("email", get_email())
    query = urllib.parse.urlencode(request_params)
    separator = "&" if "?" in url else "?"
    request = urllib.request.Request(url + separator + query, method="GET")
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def harvest(query, email, raw_dir, manifest_path):
    last_request_at = None

    def request(url, params):
        nonlocal last_request_at
        if last_request_at is not None:
            elapsed = time.monotonic() - last_request_at
            if elapsed < MIN_REQUEST_INTERVAL:
                time.sleep(MIN_REQUEST_INTERVAL - elapsed)
        response = fetch(url, {**params, "email": email})
        last_request_at = time.monotonic()
        return response

    search = request(
        EUTILS_URL + "esearch.fcgi",
        {"db": "pubmed", "term": query, "retmode": "json", "retmax": 10000},
    )
    result = json.loads(search.decode("utf-8"))["esearchresult"]
    count = int(result["count"])
    pmids = result["idlist"]
    if count != len(pmids):
        raise ValueError(
            f"PubMed reported {count} results but returned {len(pmids)} PMIDs"
        )

    raw_path = Path(raw_dir)
    raw_path.mkdir(parents=True, exist_ok=True)
    batch_files = []
    for start in range(0, len(pmids), 200):
        batch_number = start // 200 + 1
        response = request(
            EUTILS_URL + "efetch.fcgi",
            {
                "db": "pubmed",
                "id": ",".join(pmids[start : start + 200]),
                "retmode": "xml",
            },
        )
        filename = f"batch-{batch_number:03d}.xml"
        (raw_path / filename).write_bytes(response)
        batch_files.append(filename)

    manifest = {
        "query": query,
        "run_at": datetime.now(timezone.utc).isoformat(),
        "count": count,
        "pmids": pmids,
        "batch_files": batch_files,
    }
    manifest_path = Path(manifest_path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main():
    query = read_query("notes/inclusion-criteria.md")
    email = get_email()
    date = datetime.now(timezone.utc).date().isoformat()
    raw_dir = Path("data/raw") / date
    manifest_path = Path("data/manifests") / f"{date}.json"
    manifest = harvest(query, email, raw_dir, manifest_path)
    print(f"count: {manifest['count']}")
    print(f"raw XML: {raw_dir}")
    print(f"manifest: {manifest_path}")
    return manifest


if __name__ == "__main__":
    main()
