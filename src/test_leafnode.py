import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        node = LeafNode("Hello, World!", "p", {"class": "greeting"})
        expected_html = '<p class="greeting">Hello, World!</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_tag_no_props(self):
        node = LeafNode("Hello, World!", "h1")
        expected_html = '<h1>Hello, World!</h1>'
        self.assertEqual(node.to_html(), expected_html)
        
    def test_to_html_no_tag(self):
        node = LeafNode("Just some text", None)
        expected_html = 'Just some text'
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()