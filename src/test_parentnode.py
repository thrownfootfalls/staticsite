import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_simplenest(self):
#        node = LeafNode(None, "Just words here, friend!")
#        self.assertEqual(node.to_html(), "Just words here, friend!")
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),
        "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    #TODO: more tests, once it's clearerwhat the scope of this project is




