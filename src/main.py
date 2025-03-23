from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(text_node)

    html_node = HTMLNode("a", text_node, props={"href": "https://www.boot.dev"})
    print(html_node)


if __name__ == "__main__":
    main()
