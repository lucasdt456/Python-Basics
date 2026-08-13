import logging

from obsidian_notes_to_anki.automations import menu, parse_arguments, redirect_script


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main():
    setup_logging()
    arg = parse_arguments().option

    option_selected = menu() if arg is None else arg

    logging.debug(f"Option selected: {option_selected}. Starting process...")
    redirect_script(option_selected)
    return True


if __name__ == "__main__":
    main()
