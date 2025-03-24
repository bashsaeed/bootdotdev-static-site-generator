import unittest

from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_simple_h1(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_h1_with_whitespace(self):
        md = "   #   Welcome to my site   "
        self.assertEqual(extract_title(md), "Welcome to my site")

    def test_multiple_headers_only_first_is_h1(self):
        md = """
# First Title
## Subtitle
### Smaller title
"""
        self.assertEqual(extract_title(md), "First Title")

    def test_no_h1_header_raises(self):
        md = """
## Subtitle
### Another
- Bullet point
"""
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_h1_later_in_text(self):
        md = """
Intro text

# Page Title

More text
"""
        self.assertEqual(extract_title(md), "Page Title")


if __name__ == "__main__":
    unittest.main()
