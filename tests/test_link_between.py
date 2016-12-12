import pytest
import markdown

from src.evernote_client_wrapper import EvernoteClientWrapper
from tests.en_api_token import dev_token


def test_convert_markdown_and_create_note():
    md = markdown.Markdown()
    with open('test.md', mode='r') as f:
        conv_str = md.convert(f.read())

    client = EvernoteClientWrapper(token=dev_token, sandbox=True)
    note = client.create_note(note_title='md convert test', note_content=conv_str, parent_notebook=client.get_default_notebook())
    assert 'md' in note.title


if __name__ == '__main__':
    pytest.main()
