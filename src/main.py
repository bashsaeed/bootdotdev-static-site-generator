from htmlnode import HTMLNode
from textnode import TextNode, TextType
from copy_directory import copy_directory


def main():
    copy_directory("static", "public")


if __name__ == "__main__":
    main()
