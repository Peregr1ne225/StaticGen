import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        parent = ParentNode(tag="div", children=[LeafNode(tag="p", value="Hello")])
        self.assertEqual(parent.to_html(), "<div><p>Hello</p></div>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child1</span><span>child2</span></div>",
        )

    def test_to_html_with_attributes(self):
        child_node = LeafNode("span", "child", {"class": "test"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span class="test">child</span></div>',
        )

    def test_to_html_with_nested_attributes(self):
        grandchild_node = LeafNode("b", "grandchild", {"class": "grand"})
        child_node = ParentNode("span", [grandchild_node], {"class": "child"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span class="child"><b class="grand">grandchild</b></span></div>',
        )

    def test_to_html_with_nested_attributes_and_children(self):
        grandchild_node = LeafNode("b", "grandchild", {"class": "grand"})
        child_node = ParentNode("span", [grandchild_node], {"class": "child"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span class="child"><b class="grand">grandchild</b></span></div>',
        )

    def test_error_handling(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(
            str(context.exception),
            "Parent nodes must have children",
        )
