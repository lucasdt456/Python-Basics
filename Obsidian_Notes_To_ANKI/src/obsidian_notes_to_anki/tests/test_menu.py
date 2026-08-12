#import logging
import pytest
from unittest.mock import patch
from obsidian_notes_to_anki.automations.menu import menu


@pytest.mark.parametrize(
        "input_user, expected_value",
        [
            ("1", 1),
            ("2", 2),
            ("3", 3),
        ]
)
@patch("builtins.input")
def test_option_menu_all_values(mock_input, input_user, expected_value):
    mock_input.return_value = input_user
    result = menu()
    assert result == expected_value

@patch("builtins.input", side_effect=["hola", "4", "1"])
def test_option_value_menu_iterate(mock_input, caplog):
    #caplog.set_level(logging.DEBUG)
    resultado = menu()

    assert "Insert a number (range 1 - 3)" in caplog.text
    assert "Select a good option (range 1-3)" in caplog.text
    assert "The user selected a good option" in caplog.text

    assert len(caplog.records) == 3
    assert caplog.records[0].levelname == "WARNING"
    assert caplog.records[1].levelname == "WARNING"
    assert caplog.records[2].levelname == "INFO"

    assert resultado == 1
    assert mock_input.call_count == 3

@patch("builtins.input", side_effect=KeyboardInterrupt)
def test_menu_keyboard_interrupt(mock_input, caplog):

    with pytest.raises(SystemExit) as exception:
        menu()

    assert exception.value.code == 0

    assert "(Ctrl + C): Exiting the script..." in caplog.text
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"

    assert mock_input.call_count == 1