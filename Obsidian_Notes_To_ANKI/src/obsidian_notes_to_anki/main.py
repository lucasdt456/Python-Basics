from obsidian_notes_to_anki.automations import menu, parse_arguments, redirect_script


def main():
    if parse_arguments().option is None:
        option_selected = menu()

    else:
        option_selected = parse_arguments().option

    redirect_script(option_selected)
    return True


if __name__ == "__main__":
    main()
