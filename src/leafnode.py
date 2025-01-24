from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # is tag mandatory here just to get over the faux pas of rearranging
        # the arguments? Or is it because we know the tag will exist, because
        # otherwise the leaf node couldn't be refined? But then. we allow
        # later for the tag to be None...
        super().__init__(tag, value, None, props) # children forbidden

    def to_html(self):
        if self.value is None:
            raise ValueError
            # It feels weird to raise this here, instead of catching it in
            # the leaf node's constructor. Why here?
        elif self.tag is None:
            assert type(self.value) == str # just checking!
            return self.value # the means "return" literally, yes?
        else:
            props_html = self.props_to_html()
            if props_html != "":
                props_html = " " + props_html
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
