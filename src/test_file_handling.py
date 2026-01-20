import unittest
from file_handling import extract_title

class TestFileHandling(unittest.TestCase):
    def test_extract_title(self):
        content = "# Title\n\nSome other content"
        title = extract_title(content)
        self.assertEqual(title, "Title")

    def test_extract_title_no_title(self):
        content = "We dont have a title\n\nNot here either"
        self.assertRaises(Exception, extract_title, content)


if __name__ == "__main__":
    unittest.main()