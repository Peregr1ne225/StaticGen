import unittest

from inline import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "Hello, world!"
        expected = [
            TextNode("Hello, world!", TextType.TEXT, None),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_with_all_delimiters(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("text", TextType.BOLD, None),
            TextNode(" with an ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" word and a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" and an ", TextType.TEXT, None),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT, None),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_with_some_delimiters(self):
        text = "This is **text** with an _italic_ word and a `code block`"
        expected = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("text", TextType.BOLD, None),
            TextNode(" with an ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" word and a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_with_some_delimiters_and_image(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("text", TextType.BOLD, None),
            TextNode(" with an ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" word and a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" and an ", TextType.TEXT, None),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
        ]
        self.assertEqual(text_to_textnodes(text), expected)
