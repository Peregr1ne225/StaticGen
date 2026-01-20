import unittest

from inline import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter_with_not_matching_delimiter(self):
        text = "`Hello`,` World!"
        delimiter = "`"
        node = TextNode(text, TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], delimiter, TextType.TEXT)
        self.assertEqual(
            str(context.exception),
            "Delimiter '`' not balanced in text node",
        )

    def test_split_delimiter_with_multiple_delimiters(self):
        text = "**Hello**, World!, **It's me**"
        delimiter = "**"
        expected = [
            TextNode("Hello", TextType.BOLD),
            TextNode(", World!, ", TextType.TEXT),
            TextNode("It's me", TextType.BOLD),
        ]
        self.assertEqual(
            split_nodes_delimiter(
                [TextNode(text, TextType.TEXT)], delimiter, TextType.BOLD
            ),
            expected,
        )
