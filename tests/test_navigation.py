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


class ResumeScannerCorrectnessTests(unittest.TestCase):
    def test_matches_whole_keywords_and_handles_empty_keyword_set(self):
        source = (Path(__file__).parents[1] / "resume-scanner" / "index.html").read_text(encoding="utf-8")
        self.assertIn("const resumeWords = new Set(tokenize(resumeText));", source)
        self.assertIn("resumeWords.has(keyword)", source)
        self.assertNotIn("resumeText.includes(keyword)", source)
        self.assertIn("No meaningful keywords found", source)


class Base64UnicodeCorrectnessTests(unittest.TestCase):
    def test_uses_utf8_conversion_for_unicode_text(self):
        source = (Path(__file__).parents[1] / "base64-tool" / "index.html").read_text(encoding="utf-8")
        self.assertIn("new TextEncoder().encode", source)
        self.assertIn("new TextDecoder('utf-8', { fatal: true }).decode", source)
        self.assertNotIn("btoa(document.getElementById('input').value)", source)
        self.assertNotIn("document.getElementById('output').value = atob", source)


class WordCounterCorrectnessTests(unittest.TestCase):
    def test_empty_text_has_zero_lines(self):
        source = (Path(__file__).parents[1] / "word-counter" / "index.html").read_text(encoding="utf-8")
        self.assertIn("const lineCount = text ? text.split('\\n').length : 0;", source)
        self.assertIn("document.getElementById('lines').textContent = lineCount;", source)


class FreelanceRateCalculatorCorrectnessTests(unittest.TestCase):
    def test_rejects_impossible_work_capacity_and_states_tax_boundary(self):
        source = (Path(__file__).parents[1] / "calculators" / "index.html").read_text(encoding="utf-8")
        self.assertIn("weeksOff < 0 || weeksOff >= 52", source)
        self.assertIn("billableHours <= 0", source)
        self.assertIn("Enter 0–51 weeks off and more than 0 billable hours per week.", source)
        self.assertIn("before personal income and self-employment taxes", source)
        self.assertNotIn("Desired Annual Net Salary", source)
        self.assertNotIn("tax overhead", source)


if __name__ == "__main__":
    unittest.main()
