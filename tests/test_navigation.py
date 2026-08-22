import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin


PRODUCTION_ROOT = "https://entempsllc.github.io/free-utility-tools/"
TOOL_PAGES = sorted(Path(__file__).parents[1].glob("*/index.html"))


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)


class ToolNavigationTests(unittest.TestCase):
    def test_every_tool_has_project_root_back_link(self):
        self.assertTrue(TOOL_PAGES)
        for page in TOOL_PAGES:
            parser = LinkParser()
            parser.feed(page.read_text(encoding="utf-8"))
            page_url = urljoin(PRODUCTION_ROOT, f"{page.parent.name}/")
            resolved = {urljoin(page_url, href) for href in parser.links}
            with self.subTest(page=str(page)):
                self.assertIn(PRODUCTION_ROOT, resolved)

    def test_tool_links_do_not_escape_to_account_root(self):
        account_root = "https://entempsllc.github.io/"
        for page in TOOL_PAGES:
            parser = LinkParser()
            parser.feed(page.read_text(encoding="utf-8"))
            page_url = urljoin(PRODUCTION_ROOT, f"{page.parent.name}/")
            with self.subTest(page=str(page)):
                self.assertNotIn(account_root, {urljoin(page_url, href) for href in parser.links})


class PasswordGeneratorTrustTests(unittest.TestCase):
    def test_secure_randomness_claim_uses_web_crypto(self):
        source = (Path(__file__).parents[1] / "password-generator" / "index.html").read_text(encoding="utf-8")
        self.assertIn("crypto.getRandomValues", source)
        self.assertNotIn("Math.random", source)
        self.assertIn("Select at least one character type", source)


if __name__ == "__main__":
    unittest.main()
