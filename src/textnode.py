from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text: str, text_type: TextType = TextType.PLAIN, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __repr__(self):
        return f"TextNode(text={self.text!r}, text_type={self.text_type}, url={self.url!r})"
    
    def __eq__(self, value):
        if not isinstance(value, TextNode):
            return False
        return (self.text == value.text and
                self.text_type == value.text_type and
                self.url == value.url)