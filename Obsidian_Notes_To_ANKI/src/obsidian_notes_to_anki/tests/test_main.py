import pytest
from unittest.mock import patch
from obsidian_notes_to_anki.main import main

@pytest.mark.parametrize(
        "input_args, expected_result",
        [
            (["main.py", "-o", "3"], True), 
            (["main.py", "--option", "2"], True), 
            (["main.py", "-o", "1"], True), 

        ]
)
@patch("obsidian_notes_to_anki.main.redirect_script")
def test_main_correct_with_argparse(mock_redirect, monkeypatch, input_args, expected_result):
    monkeypatch.setattr("sys.argv", input_args)
    assert main() == expected_result

    option = int(input_args[-1])
    mock_redirect.assert_called_once_with(option)


@pytest.mark.parametrize(
        "invalid_arg",
        [
            "hello",
            "bye",
            "5",
            "6",
        ]
)
def test_main_failured_with_argparse(monkeypatch, capsys, invalid_arg):
    monkeypatch.setattr("sys.argv", ["main.py", "-o", invalid_arg])

    with pytest.raises(SystemExit) as excep:
        main()

    assert excep.value.code == 2

    exit = capsys.readouterr()
    assert "error: argument -o/--option:" in exit.err


@pytest.mark.parametrize(
        "input_user, expected_value",
        [
            ("1", 1),
            ("2", 2),
            ("3", 3),
        ]
)
@patch("builtins.input")
@patch("obsidian_notes_to_anki.main.redirect_script")
def test_main_correct_without_args(mock_redirect, mock_input, monkeypatch, input_user, expected_value):
    monkeypatch.setattr("sys.argv", ["main.py"])
    mock_input.return_value = input_user
    assert main() == True
    mock_redirect.assert_called_once_with(expected_value)

@patch("builtins.input")
@patch("obsidian_notes_to_anki.main.redirect_script")
def test_main_recorvers_from_invalid_menu_input(mock_redirect, mock_input, monkeypatch):
    monkeypatch.setattr("sys.argv", ["main.py"])
    mock_input.side_effect = ["hello", "4", "1"]
    assert main() == True
    mock_redirect.assert_called_once_with(1)
    assert mock_input.call_count == 3