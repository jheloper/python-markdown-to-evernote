import pytest
import markdown


def test_convert_markdown():
    md = markdown.Markdown()
    result = md.convert('#hello, world!')
    assert 'h1' in result


def test_read_markdown_file():
    md = markdown.Markdown()
    with open('test.md', mode='r') as f:
        result = md.convert(f.read())

    assert 'h1' in result


if __name__ == '__main__':
    pytest.main()
