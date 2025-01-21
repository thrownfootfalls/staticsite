import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        self.assertEqual(
            TextNode("Let's find out if it's Tuesday", TextType.ITALIC,
                     "https://www.isittuesday.co.uk"),
            TextNode("Let's find out if it's Tuesday", TextType.ITALIC,
                     "https://www.isittuesday.co.uk"))

    def test_not_eq_text(self):
        self.assertNotEqual(
            TextNode("This is a text node", TextType.BOLD),
            TextNode("This is also a text node", TextType.BOLD)
            )

    def test_not_eq_type(self):
        self.assertNotEqual(
            TextNode("This is a text node", TextType.BOLD),
            TextNode("This is a text node", TextType.NORMAL)
            )

    def test_not_eq_url(self):
        self.assertNotEqual(
            TextNode("This is a text node", TextType.BOLD),
            TextNode("This is a text node", TextType.BOLD,
                     "https://www.isittuesday.co.uk")
            )



if __name__ == "__main__":
    unittest.main()
