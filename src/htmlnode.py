class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        if self.props is None:
            self.props = {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return " ".join(
            [f'{key}="{value}"' for key, value in self.props.items()]
            )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        #TODO: figure out how to handle quotes that should sometimes be
        # there, but not always (e.g. for None)
