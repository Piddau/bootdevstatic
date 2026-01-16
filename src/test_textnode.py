import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_url_is_none_by_default(self):
        node = TextNode("Sample text")
        self.assertIsNone(node.url)
    
    def test_type_is_plain_by_default(self):
        node = TextNode("Sample text")
        self.assertEqual(node.text_type, TextType.PLAIN)

if __name__ == "__main__":
    unittest.main()