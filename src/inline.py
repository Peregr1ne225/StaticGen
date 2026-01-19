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
    images_list = []
    pattern = r"!\[[^\[\]\(\)]*\]\([^\[\]\(\)]*\)"
    matches = re.findall(pattern, text)
    for match in matches:
        alt, img_url = match.split("](")
        images_list.append((alt.strip("!["), img_url.strip(")")))

    return images_list


def extract_markdown_links(text):
    links_list = []
    pattern = r"(?<!!)\[[^\[\]\(\)]*\]\([^\[\]\(\)]*\)"
    matches = re.findall(pattern, text)
    for match in matches:
        alt, url = match.split("](")
        links_list.append((alt.strip("!["), url.strip(")")))

    return links_list
