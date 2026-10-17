import csv
import json
import tempfile
import time
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

import parse


FIXTURES = Path(__file__).parent / "fixtures"
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


class ParseTests(unittest.TestCase):
    def test_full_record(self):
        rows = parse.parse_file(FIXTURES / "full.xml")

        self.assertEqual(rows, [{
            "pmid": "12345678",
            "title": "A Structured Study",
            "year": "2024",
            "journal": "Journal of Testing",
            "abstract": "BACKGROUND: Adults completed tasks. METHODS: Researchers measured completion.",
            "publication_types": "Clinical Trial; Randomized Controlled Trial",
            "doi": "10.1000/example.doi",
            "pmcid": "PMC1234567",
        }])

    def test_minimal_record_uses_medline_date_year(self):
        rows = parse.parse_file(FIXTURES / "minimal.xml")

        self.assertEqual(rows, [{
            "pmid": "87654321",
            "title": "A Minimal Study",
            "year": "2019",
            "journal": "Journal of Simple Tests",
            "abstract": "",
            "publication_types": "",
            "doi": "",
            "pmcid": "",
        }])

    def test_realistic_record_uses_the_right_elements(self):
        rows = parse.parse_file(FIXTURES / "realistic.xml")
        rows_by_pmid = {row["pmid"]: row for row in rows}

        self.assertEqual(rows_by_pmid["33333333"]["year"], "2024")
        self.assertEqual(rows_by_pmid["33333333"]["abstract"], "Real abstract.")
        self.assertEqual(rows_by_pmid["33333333"]["doi"], "10.1000/real.doi")
        self.assertEqual(rows_by_pmid["33333333"]["pmcid"], "PMC7654321")
        self.assertEqual(rows_by_pmid["44444444"]["year"], "2018")

    def test_billion_laughs_finishes_quickly_with_an_exception(self):
        started = time.monotonic()

        with self.assertRaises(ET.ParseError):
            parse.parse_file(FIXTURES / "billion_laughs.xml")

        self.assertLess(time.monotonic() - started, 5)

    def test_external_entity_does_not_read_secret_file(self):
        with tempfile.TemporaryDirectory() as directory:
            secret_path = Path(directory) / "secret.txt"
            secret_path.write_text("SECRET-CANARY", encoding="utf-8")
            xml_path = Path(directory) / "external.xml"
            xml_path.write_text(
                """<!DOCTYPE PubmedArticleSet [
<!ENTITY secret SYSTEM \"SECRET_PATH\">
]>
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation>
      <PMID>11111111</PMID>
      <Article>
        <ArticleTitle>&secret;</ArticleTitle>
        <Journal><Title>Journal of Safety Tests</Title>
          <JournalIssue><PubDate><Year>2024</Year></PubDate></JournalIssue>
        </Journal>
      </Article>
    </MedlineCitation>
    <PubmedData />
  </PubmedArticle>
</PubmedArticleSet>
""".replace("SECRET_PATH", secret_path.as_posix()),
                encoding="utf-8",
            )

            try:
                rows = parse.parse_file(xml_path)
            except ET.ParseError:
                return

        self.assertNotIn("SECRET-CANARY", str(rows))

    def test_check_expat_rejects_old_version(self):
        with self.assertRaises(RuntimeError):
            parse.check_expat("expat_2.7.1")
        parse.check_expat("expat_2.7.4")

    def test_parse_harvest_rejects_manifest_pmid_missing_from_xml(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw_dir = root / "raw"
            raw_dir.mkdir()
            (raw_dir / "batch-001.xml").write_bytes(
                (FIXTURES / "full.xml").read_bytes()
            )
            manifest_path = root / "manifest.json"
            manifest_path.write_text(
                json.dumps({"pmids": ["99999999"]}), encoding="utf-8"
            )

            with self.assertRaisesRegex(Exception, "99999999"):
                parse.parse_harvest(raw_dir, manifest_path, root / "out.csv")

    def test_write_csv_round_trips_special_title_and_header(self):
        row = {
            "pmid": "12345678",
            "title": 'Comma, quote "and\nline break',
            "year": "2024",
            "journal": "Journal of Testing",
            "abstract": "Abstract",
            "publication_types": "Clinical Trial",
            "doi": "10.1000/example.doi",
            "pmcid": "PMC1234567",
        }

        with tempfile.TemporaryDirectory() as directory:
            csv_path = Path(directory) / "rows.csv"
            parse.write_csv([row], csv_path)
            with csv_path.open(newline="", encoding="utf-8") as file:
                rows = list(csv.reader(file))

        self.assertEqual(rows[0], COLUMNS)
        self.assertEqual(rows[1], [row[column] for column in COLUMNS])


if __name__ == "__main__":
    unittest.main()
