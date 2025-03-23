import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
