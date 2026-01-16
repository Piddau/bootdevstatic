
class HTMLNode:
    def __init__(self):
        self.tag = None
        self.value = None
        self.children = []
        self.props = {}

    def to_html(self):
        raise NotImplementedError("HTML Node to_html method not implemented")

    def props_to_html(self):
        pass