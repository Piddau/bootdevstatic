from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag, props=None):
        super().__init__()
        self.value = value
        self.tag = tag
        self.props = props if props is not None else {}
        self.children = None

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML")
        if self.tag is None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"