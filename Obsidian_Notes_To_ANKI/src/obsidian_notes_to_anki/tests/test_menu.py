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
def test_option_value_menu_iterate(mock_input):
    resultado = menu()
    assert resultado == 1