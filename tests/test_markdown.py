import unittest
import markdown


class MarkdownTest(unittest.TestCase):

    def setUp(self):
        self.md = markdown.Markdown()

    def test_convert_markdown(self):
        result = self.md.convert('#hello, world!')
        self.assertIn('h1', result)

    def test_read_markdown_file(self):
        with open('test.md', mode='r') as f:
            result = self.md.convert(f.read())
        self.assertIn('h1', result)

    def test_convert_markdown_with_newline(self):
        result = self.md.convert('#hello, world!\n##hi!')
        self.assertIn('h2', result)


if __name__ == '__main__':
    unittest.main()
