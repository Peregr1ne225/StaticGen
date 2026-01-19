import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        if delimiter not in old_node.text:
            raise ValueError(f"Delimiter '{delimiter}' not found in text node")
        delimiter_count = old_node.text.count(delimiter)
        if delimiter_count % 2 != 0:
            raise ValueError(f"Delimiter '{delimiter}' not balanced in text node")
        new_node = []
        parts = old_node.text.split(delimiter)
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 != 0:
                new_node.append(TextNode(part, text_type))
            else:
                new_node.append(TextNode(part, TextType.TEXT))
        new_nodes.extend(new_node)
    print(new_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]\(\)]*)\]\(([^\[\]\(\)]*)\)"
    matches = re.findall(pattern, text)

    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]\(\)]*)\]\(([^\[\]\(\)]*)\)"
    matches = re.findall(pattern, text)

    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        extract_node = []
        extract_images = extract_markdown_images(old_node.text)
        if len(extract_images) == 0:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        for link in extract_images:
            text = text.split(f"[{link[0]}]({link[1]})", 1)
            if text[0] != "":
                extract_node.append(TextNode(text[0], TextType.TEXT))
            extract_node.append(TextNode(link[0], TextType.LINK, link[1]))
            text = text[1]

        if len(text) > 0 and text != "":
            extract_node.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(extract_node)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        extract_node = []
        extract_links = extract_markdown_links(old_node.text)
        if len(extract_links) == 0:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        for link in extract_links:
            text = text.split(f"[{link[0]}]({link[1]})", 1)
            if text[0] != "":
                extract_node.append(TextNode(text[0], TextType.TEXT))
            extract_node.append(TextNode(link[0], TextType.LINK, link[1]))
            text = text[1]

        if len(text) > 0 and text != "":
            extract_node.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(extract_node)

    return new_nodes


if __name__ == "__main__":
    print(
        split_nodes_image(
            [
                TextNode(
                    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
                    TextType.TEXT,
                )
            ]
        )
    )
