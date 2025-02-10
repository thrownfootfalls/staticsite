import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_batch(self):
        # I'm trying out a slightly different method

#        node = TextNode("Boots **really** likes baked salmon", TextType.BOLD)
        node = TextNode("Plain old text", TextType.BOLD)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
                         [TextNode("Plain old text", TextType.NORMAL)]
            )

        node = TextNode("Exciting **bold** text", TextType.BOLD)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
                         [
                             TextNode("Exciting ", TextType.NORMAL),
                             TextNode("bold", TextType.BOLD),
                             TextNode(" text", TextType.NORMAL)
                          ]
            )

