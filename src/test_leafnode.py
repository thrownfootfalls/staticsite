import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_plaintext(self):
        node = LeafNode(None, "Just words here, friend!")
        self.assertEqual(node.to_html(), "Just words here, friend!")

    def test_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),
                    '<a href="https://www.google.com">Click me!</a>')





