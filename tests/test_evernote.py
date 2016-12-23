import unittest
from evernote.edam.notestore.ttypes import NoteMetadata
from evernote.edam.type.ttypes import Note

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
        notes_data = self.ecw.get_notes_data_by_parameter(notebook_guid=self.ecw.get_notebooks()[0].guid)
        self.assertIsInstance(notes_data[0], NoteMetadata)

    def test_create_note(self):
        title = 'test note'
        result = self.ecw.create_note(title, 'this is test note.', self.ecw.get_notebooks()[0])
        self.assertEqual(result.title, title)

    def test_get_tags(self):
        tags = self.ecw.get_tags()
        self.assertIsNotNone(tags)

    def test_get_tag_by_tag_name(self):
        tag_name = 'mte'
        tag = self.ecw.get_tag_by_tag_name(tag_name)
        self.assertEqual(tag.name, tag_name)

    def test_get_notes_data_by_tag(self):
        tag_name = 'mte'
        tag = self.ecw.get_tag_by_tag_name(tag_name)
        notes_data = self.ecw.get_notes_data_by_parameter(tag_guids=[tag.guid])
        self.assertIsInstance(notes_data[0], NoteMetadata)

    def test_get_notes_by_tag(self):
        tag_name = 'mte'
        tag = self.ecw.get_tag_by_tag_name(tag_name)
        notes_data = self.ecw.get_notes_data_by_parameter(tag_guids=[tag.guid])
        notes_guid = [data.guid for data in notes_data]
        note = self.ecw.get_note_by_guid(notes_guid[0])
        self.assertIsInstance(note, Note)

    def test_convert_note_content_to_text(self):
        tag_name = 'mte'
        tag = self.ecw.get_tag_by_tag_name(tag_name)
        notes_data = self.ecw.get_notes_data_by_parameter(tag_guids=[tag.guid])
        notes_guid = [data.guid for data in notes_data]
        note = self.ecw.get_note_by_guid(notes_guid[0])
        converted_content = self.ecw.convert_note_content_to_text(note.content)
        self.assertNotIn('<div>', converted_content)


if __name__ == '__main__':
    unittest.main()
