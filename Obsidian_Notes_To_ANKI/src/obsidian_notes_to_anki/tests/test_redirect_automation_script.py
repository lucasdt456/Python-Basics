import pytest
from unittest.mock import patch
from obsidian_notes_to_anki.automations.redirect_automation_script import redirect_script


@pytest.mark.parametrize(
    "option_case, expected_value",
    [
        (1, True)
        #(2, True),
        #(3, True)
    ]
)
@patch("builtins.input")
@patch("obsidian_notes_to_anki.automations.redirect_automation_script.comment_the_file")
def test_correct_redirectetion(mock_comment_file, mock_input, tmp_path, option_case, expected_value):
    fake_file = tmp_path / "example.md"
    fake_file.touch()
    mock_input.return_value = str(fake_file)
    assert redirect_script(option_case) == expected_value
    mock_comment_file.assert_called_once_with(fake_file)


# delete when implement the 2 and 3 options
@pytest.mark.parametrize(
    "option_case, expected_value",
    [
        
        (2, True),
        (3, True)
    ]
)
@patch("obsidian_notes_to_anki.automations.redirect_automation_script.comment_the_file")
def test_two_three_options(mock_comment_file, option_case, expected_value, capsys):
    assert redirect_script(option_case) == expected_value

    mock_comment_file.assert_not_called()
    
    output_print = capsys.readouterr()
    assert "In process...." in output_print.out

    with capsys.disabled():
        print(f"\n--- PRINTS CAPTURADOS (Opción {option_case}) ---")
        print(output_print.out)
        print("---------------------------------")

@patch("builtins.input")
@patch("obsidian_notes_to_anki.automations.redirect_automation_script.comment_the_file")
def test_redirect_option_1_recovers_from_bad_path(mock_comment_file, mock_input, tmp_path, capsys):

    fake_file = tmp_path / "example.md"
    fake_file.touch()

    mock_input.side_effect = ["fake/full/random/path/dont/exist.md", str(fake_file)]

    assert redirect_script(1) == True
    assert mock_input.call_count == 2

    mock_comment_file.assert_called_once_with(fake_file)

    output_print = capsys.readouterr()
    assert "Pass the correct path" in output_print.out

    with capsys.disabled():
        print(f"\n--- PRINTS CAPTURADOS ---")
        print(output_print.out)
        print("---------------------------------")


@patch("builtins.input")
def test_redirect_option_1_keyboard_interrupt(mock_input):
    mock_input.side_effect = KeyboardInterrupt

    with pytest.raises(SystemExit) as exception_info:
        redirect_script(1)

    assert "Exiting the script..." in str(exception_info.value)