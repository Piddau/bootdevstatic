
class HTMLNode:
    def __init__(self):
        self.tag = None
        self.value = None
        self.children = []
        self.props = {}

    def to_html(self):
        raise NotImplementedError("HTML Node to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        html_props = ""
        for prop, val in self.props.items():
            html_props += f" {prop}=\"{val}\""
        return html_props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

