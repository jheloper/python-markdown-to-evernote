import unittest
import markdown

from src.evernote_client_wrapper import EvernoteClientWrapper
from tests.en_api_token import dev_token


class EvernoteAndMarkdownTest(unittest.TestCase):

    def test_convert_markdown_and_create_note(self):
        md = markdown.Markdown()
        with open('tests/test.md', mode='r') as f:
            conv_str = md.convert(f.read())

        client = EvernoteClientWrapper(token=dev_token, sandbox=True)
        note_title = 'md convert test'
        note = client.create_note(note_title=note_title, note_content=conv_str,
                              parent_notebook=client.get_default_notebook())
        self.assertEqual(note_title, note.title)


if __name__ == '__main__':
    unittest.main()
