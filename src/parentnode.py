from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        self.value = None
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if not self.children:
            raise ValueError("ParentNode must have children to convert to HTML")
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"