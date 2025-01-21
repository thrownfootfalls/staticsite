from enum import Enum

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        # Consider them equal if all their fields are the same.
        return (self.text == other_node.text and
                self.text_type == other_node.text_type and
                self.url == other_node.url)

    def __repr__(self):
#        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        return f'TextNode("{self.text}", "{self.text_type}", "{self.url}")'

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINK = "Links"
    IMAGE = "Images"
