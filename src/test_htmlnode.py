import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode()
        node.props = {"href": "https://www.example.com"}
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode()
        node.props = {
            "href": "https://www.example.com",
            "target": "_blank",
            "rel": "noopener"
        }
        expected = ' href="https://www.example.com" target="_blank" rel="noopener"'
        self.assertEqual(node.props_to_html(), expected)