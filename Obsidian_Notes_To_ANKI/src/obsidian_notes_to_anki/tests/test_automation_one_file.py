from pathlib import Path

import pytest

from obsidian_notes_to_anki.automations.automation_one_file import comment_the_file

content1 = """
TARGET DECK: Name of your deck

Question1 #basic
Answer1

more...
"""

content2 = """
TARGET DECK
Name of your deck

Question1 #basic
Answer1

more...
"""

content3 = """
TARGET DECK
Name of your deck
Question1 #basic
Answer1

more...
"""

content4 = """
TARGET DECK: Name of your deck    
Question1 #basic
Answer1

more...
"""

content5 = """
Question1 #basic
Answer1

TARGET DECK: Name of your deck
"""

content6 = """
Question1 #basic
Answer1

TARGET DECK
Name of your deck
"""

content7 = """
Question1 #basic
Answer1

TARGET DECK
Name of your deck

Question2 #basic
Answer2
"""

content8 = """
Question1 #basic
Answer1

TARGET DECK: Name of your deck

Question2 #basic
Answer2
"""


@pytest.mark.parametrize(
    "content, expected",
    [
        # good content (return Path):
        (content1, "!These are annotated¡"),
        (content2, "!These are annotated¡"),
        (content3, "!These are annotated¡"),
        (content4, "!These are annotated¡"),
        (content5, "!These are annotated¡"),
        (content6, "!These are annotated¡"),
        (content7, "!These are annotated¡"),
        (content8, "!These are annotated¡"),
    ],
)
def test_automate_one_file_correct(tmp_path, content, expected):
    full_path = tmp_path / "correct.md"
    full_path.write_text(content, encoding="utf-8")

    final_content = comment_the_file(full_path)
    assert isinstance(final_content, Path), (
        "Function return False (content don't modify). UNEXPECTED FAILURE. It was expected to be the modified file (return Path)."
    )

    final_content_text = final_content.read_text(encoding="utf-8")
    assert expected in final_content_text


content9 = """
%%

TARGET DECK: Name of your deck

!These are annotated¡

%%

Question1 #basic
Answer1

more...
"""

content10 = """
%%

TARGET DECK
Name of your deck
!These are annotated¡

%%

Question1 #basic
Answer1

more...
"""

content11 = """
Question1 #basic
Answer1

%%

TARGET DECK: Name of your deck
!These are annotated¡

%%
"""

content12 = """
Question1 #basic
Answer1

%%

TARGET DECK
Name of your deck
!These are annotated¡

%%
"""

content13 = """
Question1 #basic
Answer1

%%

TARGET DECK
Name of your deck
!These are annotated¡

%%


Question2 #basic
Answer2
"""

content14 = """
Question1 #basic
Answer1

%%

TARGET DECK: Name of your deck

!These are annotated¡

%%

Question2 #basic
Answer2
"""


@pytest.mark.parametrize(
    "content, expected",
    [
        (content9, False),
        (content10, False),
        (content11, False),
        (content12, False),
        (content13, False),
        (content14, False),
        ("", False),
        ("Random note without the target keyword", False),
    ],
)
def test_automate_one_file_should_fail(tmp_path, content, expected):
    full_path = tmp_path / "fail.md"
    full_path.write_text(content, encoding="utf-8")

    final_content = comment_the_file(full_path)
    assert final_content is expected, (
        f"\nThe function return -> {type(final_content)} and expect -> {(expected)}"
    )
