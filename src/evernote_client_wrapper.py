from evernote.api.client import *
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import Note


class EvernoteClientWrapper:
    def __init__(self, **kwargs):
        self.client = EvernoteClient(token=kwargs['token'], sandbox=kwargs['sandbox'])

    def get_user(self):
        return self.client.get_user_store().getUser()

    def get_notebooks(self):
        return self.client.get_note_store().listNotebooks()

    def get_default_notebook(self):
        return self.client.get_note_store().getDefaultNotebook()

    '''
    def get_notebook_by_notebook_name(self, notebook_name):
        for notebook in self.get_notebooks():
            if notebook_name in notebook.name:
                return notebook
    '''

    def get_notes_by_parameter(self, **kwargs):
        note_filter = NoteFilter(words=kwargs.get('words'),
                                 notebookGuid=kwargs.get('notebook_guid'), tagGuids=kwargs.get('tag_guids'))
        note_metadata_list = self.client.get_note_store().\
            findNotesMetadata(note_filter, 0, 10000, NotesMetadataResultSpec(includeNotebookGuid=True,
                                                                             includeTitle=True, includeTagGuids=True))
        return note_metadata_list.notes

    def create_note(self, note_title, note_content, parent_notebook):

        n_body = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        n_body += "<!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml2.dtd\">"
        n_body += "<en-note>%s</en-note>" % note_content
        note = Note()
        note.title = note_title
        note.content = n_body

        if parent_notebook and hasattr(parent_notebook, 'guid'):
            note.notebookGuid = parent_notebook.guid

        return self.client.get_note_store().createNote(note)
