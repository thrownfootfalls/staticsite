from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        #(self, tag=None, value=None, children=None, props=None)

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tags found for this ParentNode")
        elif self.children is None: # or does it mean, if this is empty?
            raise ValueError("no children found for this ParentNode")

    def to_html(self):
        child_htmls = [child.to_html() for child in self.children]
        #print(":) "*30)
        #print(child_htmls)
        #print(":) "*30)
        return f'<{self.tag}{self.props_to_html()}>{"".join(child_htmls)}</{self.tag}>'
        #stray space between tag and empty props?
        #I'm not sure how to, in this file, split the code across lines
