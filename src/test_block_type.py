import unittest

from block import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# Heading 1\n## Heading 2\n### Heading 3\n#### Heading 4\n##### Heading 5\n###### Heading 6"
        expected = BlockType.HEADING
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)

    def test_block_to_block_type_paragraph(self):
        block = "Paragraph"
        expected = BlockType.PARAGRAPH
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)

    def test_block_to_block_type_quote(self):
        block = "> Quote"
        expected = BlockType.QUOTE
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)

    def test_block_to_block_type_unordered_list(self):
        block = "- Unordered List Item 1\n- Unordered List Item 2"
        expected = BlockType.UNORDERED_LIST
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)

    def test_block_to_block_type_ordered_list(self):
        block = "1. Ordered List Item 1\n2. Ordered List Item 2"
        expected = BlockType.ORDERED_LIST
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)

    def test_block_to_block_type_code_block(self):
        block = "```\nCode Block\n```"
        expected = BlockType.CODE
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)

    def test_block_to_block_type_mix(self):
        block = "# Heading 1\n## Heading 2\n### Heading 3\n#### Heading 4\n##### Heading 5\n###### Heading 6\nParagraph\n> Quote\n- Unordered List Item 1\n- Unordered List Item 2\n1. Ordered List Item 1\n2. Ordered List Item 2\n```\nCode Block\n```"
        expected = BlockType.PARAGRAPH
        actual = block_to_block_type(block)
        self.assertEqual(actual, expected)
