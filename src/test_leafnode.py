import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_node_creation(self):
        node = LeafNode("div", "Hello")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello")
        self.assertEqual(node.to_html(), "<div>Hello</div>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me</a>')


if __name__ == "__main__":
    unittest.main()
