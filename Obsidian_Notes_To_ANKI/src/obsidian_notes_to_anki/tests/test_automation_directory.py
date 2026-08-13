import pytest

from obsidian_notes_to_anki.automations.automation_directory import (
    comment_one_directory,
)

content1 = """
TARGET DECK: Name of your deck

Question1 #basic
Answer1

more...
"""

content2 = """
%%

TARGET DECK: Name of your deck

!These are annotated¡

%%

Question1 #basic
Answer1

more...
"""


@pytest.fixture
def create_directory(tmp_path):

    subdir1 = tmp_path / "subdir1"
    subdir1.mkdir()

    subdir2 = tmp_path / "subdir1" / "subdir2"
    subdir2.mkdir()

    (tmp_path / "first_content.md").write_text(content1)
    (tmp_path / "subdir1" / "second_content.md").write_text(content1)
    (tmp_path / "subdir1" / "subdir2" / "third_content.md").write_text(content1)
    (tmp_path / "subdir1" / "subdir2" / "four_content_with_comments.md").write_text(
        content2
    )

    # this is not printed (because these are not .md files)
    (tmp_path / "content_empty.md").write_text("")

    (tmp_path / "bad_content.py").write_text("hello word")
    (tmp_path / "subdir1" / "bad_content2.jpg").write_text("image")

    return tmp_path


def test_direcory(create_directory):

    assert comment_one_directory(create_directory) == 3
