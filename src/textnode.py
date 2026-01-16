from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType = TextType.TEXT, url: str = None):
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
    

def text_node_to_html_node(text_node):
    from leafnode import LeafNode

    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text, tag=None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(value=text_node.text, tag="strong")
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(value=text_node.text, tag="em")
    elif text_node.text_type == TextType.CODE:
        return LeafNode(value=text_node.text, tag="code")
    elif text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError("Link TextNode must have a URL")
        return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("Image TextNode must have a URL")
        return LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")