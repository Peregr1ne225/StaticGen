import unittest

from inline import extract_markdown_images, extract_markdown_links


class TestRegexExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_from_mix(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_from_mix(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertEqual(extract_markdown_images(text), expected)
