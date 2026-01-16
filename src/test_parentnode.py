import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_add_child(self):
        child = LeafNode("Hello", "p")
        parent = ParentNode("div", [child])
        self.assertIn(child, parent.children)

    def test_to_html_with_children(self):
        child1 = LeafNode("Hello", "p")
        child2 = LeafNode("World", "p")
        parent = ParentNode("div", [child1, child2], {"class": "container"})
        expected_html = '<div class="container"><p>Hello</p><p>World</p></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("child", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_parent_without_children_throw(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_parent_without_tag_throw(self):
        child_node = LeafNode("child", "span")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()