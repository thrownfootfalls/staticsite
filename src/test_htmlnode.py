import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p", "Hello, world!", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_one_prop(self):
        node = HTMLNode("a", "Click here to find out if it is Tuesday",
                        None, {"href": "https://www.isittuesday.co.uk"})
        self.assertEqual(node.props_to_html(),
                         'href="https://www.isittuesday.co.uk"')

    def test_many_props(self):
        node = HTMLNode("h1", "Secret Negotiations With Martians Revealed!!!!!", None, {"verisimilitude": "not much", "clickability": 78.1}) # I don't know enough actual properties
        self.assertEqual(node.props_to_html(),
                         f'verisimilitude="not much" clickability="78.1"')
