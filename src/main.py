from textnode import TextNode
from htmlnode import HTMLNode

def main():
    #print("hello world")
    dummy_text_node = TextNode("This is a text node", "bold",
                               "https://www.isittuesday.co.uk")
    dummy_html_node = HTMLNode("p", "Hello, world!", None, None)

    print(dummy_text_node)
    print(dummy_html_node)

if __name__ == "__main__":
    main()
