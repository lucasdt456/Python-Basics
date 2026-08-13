# import sys
import logging

import pytest

from obsidian_notes_to_anki.automations.parser import parse_arguments


@pytest.mark.parametrize(
    "input_args, expected_result",
    [
        (["main.py", "-o", "3"], 3),
        (["main.py", "--option", "2"], 2),
        (["main.py", "-o", "1"], 1),
    ],
)
def test_parse_all_arg(monkeypatch, caplog, input_args, expected_result):
    caplog.set_level(logging.DEBUG)
    monkeypatch.setattr("sys.argv", input_args)
    args = parse_arguments()
    assert args.option == expected_result


def test_parse_failed(monkeypatch, caplog):
    caplog.set_level(logging.DEBUG)
    monkeypatch.setattr("sys.argv", ["main.py", "-o", "hello"])

    with pytest.raises(SystemExit) as exception:
        parse_arguments()

    assert exception.value.code == 2
