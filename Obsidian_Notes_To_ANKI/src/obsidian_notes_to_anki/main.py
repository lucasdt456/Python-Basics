import logging
from obsidian_notes_to_anki.automations import menu, parse_arguments, redirect_script

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt= "%Y-%m-%d %H:%M:%S",
    )


def main():
    setup_logging()
    if parse_arguments().option is None:
        option_selected = menu()

    else:
        option_selected = parse_arguments().option

    logging.debug(f"Option selected: {option_selected}. Starting process...")
    redirect_script(option_selected)
    return True


if __name__ == "__main__":
    main()
