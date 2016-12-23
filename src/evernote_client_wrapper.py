from evernote.api.client import *
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import Note
import re


class EvernoteClientWrapper:

    def __init__(self, **kwargs):
        """
        :param kwargs:
        """
        self.client = EvernoteClient(token=kwargs['token'], sandbox=kwargs['sandbox'])

    def get_user(self):
        """
        :rtype: evernote.edam.type.ttypes.User
        """
        return self.client.get_user_store().getUser()

    def get_notebooks(self):
        """
        :rtype: list[evernote.edam.type.ttypes.Notebook]
        """
        return self.client.get_note_store().listNotebooks()

    def get_default_notebook(self):
        """
        :rtype: evernote.edam.type.ttypes.Notebook
        """
        return self.client.get_note_store().getDefaultNotebook()

    def get_notes_data_by_parameter(self, **kwargs):
        """
        :param kwargs:
        :rtype: list[evernote.edam.type.ttypes.Note]
        """
        note_filter = NoteFilter(words=kwargs.get('words'),
                                 notebookGuid=kwargs.get('notebook_guid'), tagGuids=kwargs.get('tag_guids'))
        note_metadata_list = self.client.get_note_store().\
            findNotesMetadata(note_filter, 0, 10000, NotesMetadataResultSpec(includeNotebookGuid=True,
                                                                             includeTitle=True, includeTagGuids=True))
        return note_metadata_list.notes

    def create_note(self, note_title, note_content, parent_notebook):
        """
        :param string note_title:
        :param string note_content:
        :param Notebook parent_notebook:
        :rtype: evernote.edam.type.ttypes.Note
        """
        n_body = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        n_body += "<!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml2.dtd\">"
        n_body += "<en-note>%s</en-note>" % note_content
        note = Note()
        note.title = note_title
        note.content = n_body

        if parent_notebook and hasattr(parent_notebook, 'guid'):
            note.notebookGuid = parent_notebook.guid

        return self.client.get_note_store().createNote(note)

    def get_tags(self):
        return self.client.get_note_store().listTags()

    def get_tag_by_tag_name(self, tag_name):
        """
        :param tag_name:
        :rtype: evernote.edam.type.ttypes.Tag
        """
        tag_list = self.get_tags()
        tag = [tag for tag in tag_list if tag.name == tag_name]
        if len(tag) == 1:
            return tag[0]
        else:
            raise Exception('Duplicate name tags exist.')

    def get_note_by_guid(self, guid):
        return self.client.get_note_store().getNote(guid, True, True, True, True)

    def convert_note_content_to_text(self, note_content):
        newline_p = re.compile(r'</div>')
        tag_p = re.compile(r'<.*>')
        return tag_p.sub('', newline_p.sub('\n', note_content))





