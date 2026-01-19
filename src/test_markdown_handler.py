import unittest

from markdown_handler import BlockTypes, BlockTypes, block_to_block_type, markdown_to_blocks

class TestMarkdownHandler(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty(self):
        md = "\n\n   \n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_markdown_to_blocks_single(self):
        md = "Single paragraph with no breaks."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Single paragraph with no breaks."])
    
    def test_markdown_to_blocks_leading_trailing(self):
        md = "\n\n  Leading and trailing spaces  \n\nAnother paragraph.\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Leading and trailing spaces", "Another paragraph."])

    def test_markdown_block_to_block_type(self):
        self.assertEqual(
            block_to_block_type("# Header 1"),
            BlockTypes.HEADER
        )
        self.assertEqual(
            block_to_block_type("- Item 1\n- Item 2"),
            BlockTypes.UNORDERED_LIST
        )
        self.assertEqual(
            block_to_block_type("1. First\n2. Second"),
            BlockTypes.ORDERED_LIST
        )
        self.assertEqual(
            block_to_block_type("```\nCode block\n```"),
            BlockTypes.CODE 
        )
        self.assertEqual(
            block_to_block_type("> This is a quote"),
            BlockTypes.QUOTE
        )
        self.assertEqual(
            block_to_block_type("Just a normal paragraph."),
            BlockTypes.PARAGRAPH
        )
    
    def test_markdown_block_to_block_type_edge_cases(self):
        self.assertEqual(
            block_to_block_type("##Header without space"),
            BlockTypes.PARAGRAPH
        )
        self.assertEqual(
            block_to_block_type("-Item without space\n-Another item"),
            BlockTypes.PARAGRAPH
        )
        self.assertEqual(
            block_to_block_type("3.Item without space\n4.Another item"),
            BlockTypes.PARAGRAPH
        )
        self.assertEqual(
            block_to_block_type("```Code block without newlines```"),
            BlockTypes.CODE
        )
        self.assertEqual(
            block_to_block_type(">Quote without space"),
            BlockTypes.PARAGRAPH
        )
        self.assertEqual(
            block_to_block_type(""),
            BlockTypes.PARAGRAPH
        )
        
if __name__ == "__main__":
    unittest.main()