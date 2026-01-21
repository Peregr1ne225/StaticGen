from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    block = markdown.split("\n\n")
    for b in block:
        b = b.strip()
        if b == "":
            continue
        blocks.append(b)
    return blocks


def block_to_block_type(block):
    lines = block.splitlines()

    if block.startswith("#"):
        all_head = True
        for line in lines:
            if not line.startswith("#"):
                all_head = False

            count = 0
            while count < len(line) and line[count] == "#":
                count += 1
            if count == 0 or count > 6:
                all_head = False
            if count >= len(line) or line[count] != " ":
                all_head = False
        if all_head is True:
            return BlockType.HEADING
        else:
            return BlockType.PARAGRAPH

    elif block.startswith("```\n"):
        if lines[0] != "```" or lines[-1] != "```":
            return BlockType.PARAGRAPH
        else:
            return BlockType.CODE

    elif block.startswith(">"):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    elif block.startswith("-"):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    elif block.startswith("1."):
        for i, line in enumerate(lines):
            if not line.startswith(f"{i + 1}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH


if __name__ == "__main__":
    markdown = """
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

Paragraph

> Quote

- Unordered List Item 1
- Unordered List Item 2

1. Ordered List Item 1
2. Ordered List Item 2

```
Code Block
```
"""
    blocks = markdown_to_blocks(markdown)
    print(blocks)
    for block in blocks:
        print(block)
        print(block_to_block_type(block))
