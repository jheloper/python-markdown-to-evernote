import unittest
import markdown


class MarkdownTest(unittest.TestCase):

    def test_convert_markdown(self):
        md = markdown.Markdown()
        result = md.convert('#hello, world!')
        self.assertIn('h1', result)

    def test_read_markdown_file(self):
        md = markdown.Markdown()
        with open('tests/test.md', mode='r') as f:
            result = md.convert(f.read())

        self.assertIn('h1', result)


if __name__ == '__main__':
    unittest.main()
