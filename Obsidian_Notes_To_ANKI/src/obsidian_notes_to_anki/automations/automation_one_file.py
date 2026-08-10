# from pathlib import Path
import os

TEXT_TO_SEARCH = "TARGET DECK"


def comment_the_file(full_path: os.PathLike) -> None:
    try:
        if full_path.exists() and full_path.is_file():
            with open(full_path, encoding="utf-8") as file_content:
                content = file_content.readlines()

                if not content:
                    print(f"The file '{full_path.name}' are empty")
                    return

                matching_lines = [
                    index
                    for index, line in enumerate(content)
                    if TEXT_TO_SEARCH in line
                ]

                if len(matching_lines) > 0:
                    with open(full_path, "w", encoding="utf-8") as file_content:
                        line = content[matching_lines[0]]
                        line2 = (
                            content[matching_lines[0] + 1]
                            if matching_lines[0] != len(content) - 1
                            else ""
                        )
                        new_content = (
                            f"%%\n\n{line}{line2}!These are annotated¡\n\n%%\n\n"
                        )
                        content[matching_lines[0]] = new_content
                        if line2 != "":
                            content[matching_lines[0] + 1] = ""
                        # file_content.seek(0)
                        # file_content.truncate()
                        file_content.writelines(content)
                        print("The changes are correct")
                        print("Exiting the script...")

                else:
                    print(
                        f"This file: '{full_path.name}' "
                        "is not a note (ANKI <-> Obsidian) "
                        "or has been modified previously in this path: {full_path}"
                    )
                    print("Exiting the script...")
                    return

        else:
            print(f"This path: '{full_path}' doesn't exist or is not a valid file")

    except FileNotFoundError as f_n_f:
        print("Error with open the file: ", f_n_f)

    except IndexError as e:
        print("Error with the file content: ", e)

    except Exception as e:
        print("General Error: ", e)
