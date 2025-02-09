from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    #print("hello world")
    dummy_text_node = TextNode("This is a text node", "BOLD",
                               "https://www.isittuesday.co.uk")
    dummy_html_node = HTMLNode("p", "Hello, world!", None, None)

    print(dummy_text_node)
    print(dummy_html_node)

    changed_node = text_node_to_html_node(dummy_text_node)
    print(changed_node)

def text_node_to_html_node(text_node):
    if text_node.text_type == "NORMAL": #says "TEXT" in the assignment.
        # is it inconsistent, or did I get it wrong the first time?
        return LeafNode(tag=None, value = text_node.text)
    elif text_node.text_type == "BOLD":
        return LeafNode(tag="b", value = text_node.text)
    elif text_node.text_type == "ITALIC":
        return LeafNode(tag="i", value = text_node.text)
    elif text_node.text_type == "CODE":
        return LeafNode(tag="code", value = text_node.text)
    elif text_node.text_type == "LINK":
        return LeafNode(tag="a", value = text_node.text, props={"href":"?"})
        #TODO: proper href
    elif text_node.text_type == "IMAGE":
        return LeafNode(tag="img", value = "", props={"src":"?", "alt": "?"})

if __name__ == "__main__":
    main()
