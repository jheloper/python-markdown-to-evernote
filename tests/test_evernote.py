import unittest
from evernote.edam.notestore.ttypes import NoteMetadata

from src.evernote_client_wrapper import EvernoteClientWrapper
from tests.en_api_token import dev_token


class EvernoteAPITest(unittest.TestCase):

    def setUp(self):
        self.ecw = EvernoteClientWrapper(token=dev_token, sandbox=True)

    def test_connect_evernote(self):
        self.assertIsNotNone(self.ecw.get_user().username)

    def test_get_notebooks(self):
        self.assertIsNotNone(self.ecw.get_notebooks())

    def test_get_notes(self):
        # TODO note filter -> note meta data -> get note guid -> finally get note...?
        notes = self.ecw.get_notes_by_parameter(notebook_guid=self.ecw.get_notebooks()[0].guid)
        self.assertIsInstance(notes[0], NoteMetadata)

    def test_create_note(self):
        title = 'test note'
        result = self.ecw.create_note(title, 'this is test note.', self.ecw.get_notebooks()[0])
        self.assertEqual(result.title, title)


if __name__ == '__main__':
    unittest.main()
