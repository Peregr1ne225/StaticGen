from textnode import TextNode, TextType


def main():
    link = "https://example.com"
    text_node = TextNode("This is some anchor text", TextType.LINK, link)
    print(text_node)


if __name__ == "__main__":
    main()
