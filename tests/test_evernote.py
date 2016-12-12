import pytest
from evernote.edam.notestore.ttypes import NoteMetadata

from src.evernote_client_wrapper import EvernoteClientWrapper
from tests.en_api_token import dev_token


@pytest.fixture()
def client_wrapper():
    return EvernoteClientWrapper(token=dev_token, sandbox=True)


def test_connect_evernote(client_wrapper):
    assert client_wrapper.get_user().username is not None


def test_get_notebooks(client_wrapper):
    assert client_wrapper.get_notebooks()

'''
def test_get_notebook_by_notebook_name(client_wrapper):
    assert client_wrapper.get_notebook_by_notebook_name('')
'''

def test_get_notes(client_wrapper):
    # TODO note filter -> note meta data -> get note guid -> finally get note...?
    notes = client_wrapper.get_notes_by_parameter(notebook_guid=client_wrapper.get_notebooks()[0].guid)
    assert type(notes[0]) is NoteMetadata


def test_create_note(client_wrapper):
    title = 'test note'
    result = client_wrapper.create_note(title, 'this is test note.', client_wrapper.get_notebooks()[0])
    assert result.title == title


if __name__ == '__main__':
    pytest.main()
