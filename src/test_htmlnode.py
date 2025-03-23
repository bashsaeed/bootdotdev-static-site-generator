import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_repr_simple_node(self):
        node = HTMLNode(tag="p", value="Hello", props={"class": "text"})
        expected = (
            "HTMLNode(tag='p', value='Hello', props={'class': 'text'}, children=None)"
        )
        self.assertEqual(repr(node), expected)

    def test_props_to_html(self):
        node = HTMLNode(props={"id": "main", "class": "container"})
        props_string = node.props_to_html()
        self.assertIn('id="main"', props_string)
        self.assertIn('class="container"', props_string)
        self.assertEqual(set(props_string.split()), {'id="main"', 'class="container"'})

    def test_nested_node_repr(self):
        child = HTMLNode(tag="span", value="World")
        parent = HTMLNode(tag="div", children=[child])
        result = repr(parent)
        self.assertIn("HTMLNode(tag='span'", result)
        self.assertIn("children=[HTMLNode(tag='span'", result)

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr_all_none(self):
        node = HTMLNode()
        expected = "HTMLNode(tag=None, value=None, props=None, children=None)"
        self.assertEqual(repr(node), expected)


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me", props={"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click me</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(
            repr(node),
            "LeafNode(tag='p', value='Hello, world!', props=None, children=None)",
        )


if __name__ == "__main__":
    unittest.main()
