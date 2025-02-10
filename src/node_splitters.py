from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        texts = old_node.text.split(delimiter)
        for i, text in enumerate(texts):
            current_type = [TextType.NORMAL, text_type][i%2] # aiternate "on" and "off"
            new_nodes.append(TextNode(text, current_type))
    return new_nodes

