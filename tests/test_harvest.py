import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import harvest


class HarvestTests(unittest.TestCase):
    def test_read_query_from_inclusion_criteria(self):
        path = Path(__file__).parents[1] / "notes" / "inclusion-criteria.md"

        query = harvest.read_query(path)

        self.assertTrue(query.startswith("(\"Attention"))
        self.assertTrue(query.endswith('"pre-post"[tiab])'))

    def test_zero_results_writes_empty_manifest_without_fetching_records(self):
        search_response = (
            b'{"esearchresult":{"count":"0","idlist":[]}}'
        )

        with tempfile.TemporaryDirectory() as raw_dir, tempfile.TemporaryDirectory() as manifest_dir:
            manifest_path = Path(manifest_dir) / "2026-10-15.json"
            with patch.object(harvest, "fetch", return_value=search_response) as fetch:
                manifest = harvest.harvest(
                    "query", "person@example.org", raw_dir, manifest_path
                )

            written_manifest = json.loads(manifest_path.read_text())
            raw_manifest_exists = (Path(raw_dir) / "manifest.json").exists()

        self.assertEqual(manifest["count"], 0)
        self.assertEqual(manifest["pmids"], [])
        self.assertEqual(written_manifest["count"], 0)
        self.assertEqual(written_manifest["pmids"], [])
        self.assertEqual(fetch.call_count, 1)
        self.assertNotIn("efetch", fetch.call_args.args[0])
        self.assertFalse(raw_manifest_exists)

    def test_consecutive_requests_are_at_least_034_seconds_apart(self):
        pmids = [str(number) for number in range(401)]
        search_response = json.dumps(
            {"esearchresult": {"count": str(len(pmids)), "idlist": pmids}}
        ).encode()
        request_times = []
        clock = {"now": 100.0}

        def fake_fetch(url, params):
            request_times.append(clock["now"])
            if "esearch" in url:
                return search_response
            return b"<PubmedArticleSet />"

        def fake_sleep(seconds):
            clock["now"] += seconds

        with tempfile.TemporaryDirectory() as raw_dir, tempfile.TemporaryDirectory() as manifest_dir:
            manifest_path = Path(manifest_dir) / "2026-10-15.json"
            with patch.object(harvest, "fetch", side_effect=fake_fetch), patch.object(
                harvest.time, "monotonic", side_effect=lambda: clock["now"]
            ), patch.object(harvest.time, "sleep", side_effect=fake_sleep):
                harvest.harvest(
                    "query", "person@example.org", raw_dir, manifest_path
                )

        intervals = [
            later - earlier
            for earlier, later in zip(request_times, request_times[1:])
        ]
        self.assertGreaterEqual(len(request_times), 3)
        self.assertTrue(all(interval >= 0.34 - 1e-9 for interval in intervals))

    def test_get_email_requires_ncbi_email(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(Exception, "NCBI_EMAIL"):
                harvest.get_email()


if __name__ == "__main__":
    unittest.main()
