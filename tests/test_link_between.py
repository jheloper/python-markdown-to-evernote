import unittest
import markdown

from src.evernote_client_wrapper import EvernoteClientWrapper
from tests.en_api_token import dev_token


class MarkdownAndEvernoteTest(unittest.TestCase):

    def setUp(self):
        self.md = markdown.Markdown()
        self.ecw = EvernoteClientWrapper(token=dev_token, sandbox=True)

    def test_convert_markdown_and_create_note(self):
        with open('test.md', mode='r') as f:
            conv_str = self.md.convert(f.read())
        note_title = 'md convert test'
        result = self.ecw.create_note(note_title=note_title, note_content=conv_str,
                                      parent_notebook=self.ecw.get_default_notebook())
        self.assertEqual(note_title, result.title)


if __name__ == '__main__':
    unittest.main()
