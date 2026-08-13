from unittest.mock import patch

import pytest

from obsidian_notes_to_anki.automations.redirect_automation_script import (
    redirect_script,
)


@pytest.mark.parametrize(
    "option_case, expected_value",
    [(1, True)],
)
@patch("builtins.input")
@patch("obsidian_notes_to_anki.automations.redirect_automation_script.comment_the_file")
def test_correct_redirectetion(
    mock_comment_file, mock_input, tmp_path, option_case, expected_value
):
    fake_file = tmp_path / "example.md"
    fake_file.touch()
    mock_input.return_value = str(fake_file)
    assert redirect_script(option_case) == expected_value
    mock_comment_file.assert_called_once_with(fake_file)


@pytest.mark.parametrize("option_case, expected_value", [(2, True), (3, True)])
@patch("builtins.input")
@patch(
    "obsidian_notes_to_anki.automations.redirect_automation_script.comment_one_directory"
)
def test_two_three_options(
    mock_comment_dir, mock_input, tmp_path, option_case, expected_value
):
    dir = tmp_path / "dir"
    dir.mkdir()
    mock_input.return_value = str(dir)
    assert redirect_script(option_case) == expected_value
    mock_comment_dir.assert_called_once_with(dir)


@patch("builtins.input")
@patch("obsidian_notes_to_anki.automations.redirect_automation_script.comment_the_file")
def test_redirect_recovers_from_bad_path(
    mock_comment_file, mock_input, tmp_path, capsys
):

    fake_file = tmp_path / "example.md"
    fake_file.touch()

    mock_input.side_effect = ["fake/full/random/path/dont/exist.md", str(fake_file)]

    assert redirect_script(1) is True
    assert mock_input.call_count == 2

    mock_comment_file.assert_called_once_with(fake_file)

    output_print = capsys.readouterr()
    assert "Pass the correct path" in output_print.out

    # with capsys.disabled():
    #     print(f"\n--- PRINTS CAPTURADOS ---")
    #     print(output_print.out)
    #     print("---------------------------------")


@patch("builtins.input", side_effect=KeyboardInterrupt)
def test_redirect_keyboard_interrupt(mock_input, caplog):

    with pytest.raises(SystemExit) as exception:
        redirect_script(1)

    assert exception.value.code == 0

    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"
    assert "(Ctrl + C): Exiting the script..." in caplog.text

    assert mock_input.call_count == 1
