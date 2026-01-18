from enum import Enum
from typing import Text

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(node):
    if node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=node.text)
    elif node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=node.text)
    elif node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=node.text)
    elif node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=node.text)
    elif node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=node.text, props={"href": node.url})
    elif node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src": node.url, "alt": node.text})
    else:
        raise ValueError(f"Unknown text type: {node.text_type}")
