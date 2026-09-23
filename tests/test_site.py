"""Checks the parked landing page is complete enough to publish."""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "tinygpt.ai"
HANDLE = "cepstrum9"
OTHER_DOMAINS = ("agenthooks.ai", "repobase.ai", "tinyrag.ai")


class SiteContractTests(unittest.TestCase):
    def test_cname_is_apex_domain(self) -> None:
        self.assertEqual(ROOT.joinpath("CNAME").read_text(encoding="utf-8").strip(), DOMAIN)

    def test_index_has_sale_cta(self) -> None:
        html = ROOT.joinpath("index.html").read_text(encoding="utf-8")
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn(f"<title>{DOMAIN} is for sale</title>", html)
        self.assertIn(f"<h1>{DOMAIN}</h1>", html)
        self.assertIn(f"https://x.com/{HANDLE}", html)
        self.assertIn(f"@{HANDLE}", html)
        self.assertIn('name="viewport"', html)
        self.assertIn('rel="canonical"', html)

    def test_index_has_no_placeholders(self) -> None:
        html = ROOT.joinpath("index.html").read_text(encoding="utf-8")
        for token in ("TODO", "TBD", "CHANGEME", "example.com"):
            self.assertNotIn(token, html)

    def test_supporting_files_exist(self) -> None:
        for name in ("404.html", "favicon.svg", "robots.txt", "sitemap.xml"):
            path = ROOT.joinpath(name)
            self.assertTrue(path.is_file(), f"missing {name}")
            self.assertGreater(path.stat().st_size, 0)

    def test_supporting_files_use_this_domain(self) -> None:
        html_404 = ROOT.joinpath("404.html").read_text(encoding="utf-8")
        index = ROOT.joinpath("index.html").read_text(encoding="utf-8")
        self.assertIn(DOMAIN, html_404)
        for other in OTHER_DOMAINS:
            self.assertNotIn(other, html_404)
            self.assertNotIn(other, index)

    def test_robots_and_sitemap_point_at_domain(self) -> None:
        robots = ROOT.joinpath("robots.txt").read_text(encoding="utf-8")
        sitemap = ROOT.joinpath("sitemap.xml").read_text(encoding="utf-8")
        self.assertIn("Allow: /", robots)
        self.assertIn(f"https://{DOMAIN}/sitemap.xml", robots)
        self.assertIn(f"https://{DOMAIN}/", sitemap)


if __name__ == "__main__":
    unittest.main()
