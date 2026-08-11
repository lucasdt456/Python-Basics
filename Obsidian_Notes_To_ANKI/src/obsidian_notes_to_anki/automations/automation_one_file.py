# import os
# import sys
from pathlib import Path


TEXT_TO_SEARCH = "TARGET DECK"


def comment_the_file(full_path: Path) -> Path | bool:

    find = False

    try:
        if full_path.exists() and full_path.is_file():
            content = full_path.read_text(encoding="utf-8")

            if not content:
                print(f"The file '{full_path.name}' are empty")
                return False

            lines = content.splitlines(keepends=True)

            for line in lines:
                if "!These are annotated¡" in line:
                    print(
                    f"This file: '{full_path.name}' "
                    "is not a note (ANKI <-> Obsidian) "
                    f"or has been modified previously (contains the comment to disable the note) in this path: {full_path}"
                    )
                    print("Exiting the script...")
                    return False

            for index, line in enumerate(lines):
                if TEXT_TO_SEARCH in line:

                    line1 = lines[index]
                    line2 = ""
                    if index != (len(lines) - 1):
                        second_line_is_question = ("#basic" in lines[index + 1]) or ("START" in lines[index + 1])
                        line2 = lines[index + 1] if not second_line_is_question else ""
                    lines[index] = f"%%\n\n{line1}{line2}!These are annotated¡\n\n%%\n\n"
                    find = True
                    if line2 != "":
                        lines[index + 1] = ""
                    break

            if find:
                content = "".join(lines)
                full_path.write_text(content)
                print("The changes are correct")    
                print("Exiting the script...")
                return full_path

            else:
                print(
                f"This file: '{full_path.name}' "
                "is not a note (ANKI <-> Obsidian) "
                f"or does not contain: 'TARGET DECK' in this path: {full_path}"
                )
                print("Exiting the script...")
                return False
            
        else:
            print(f"This path: '{full_path}' doesn't exist or is not a valid file")
            return False

    except FileNotFoundError as f_n_f:
        print("Error with open the file: ", f_n_f)
        return False

    except IndexError as e:
        print("Error with the file content: ", e)
        return False

    except OSError as e:
        print("Error with OS/path: ", e)
        return False

    except AttributeError as e:
        print("Path Error: ", e)
        return False

    except Exception as e:
        print("General Error: ", e)
        return False
