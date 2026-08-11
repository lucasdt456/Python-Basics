import sys
from pathlib import Path
from .automation_one_file import comment_the_file


def redirect_script(option):
    match option:
        case 1:
            print("You're selected the option 1: Clear only 1 file (quickly)")
            while True:
                try:
                    path_input = input("Pass me the full path (with file): ")
                    path_input = path_input.strip("'\"")
                    path_input = Path(path_input)

                    if path_input.exists() and path_input.is_file():
                        comment_the_file(path_input)
                        return True
                    else:
                        print("Pass the correct path (or exit Ctrl + C)...")

                except Exception as e:
                    print(
                        "Error with the input path (check the file, directory, full path...): ",
                        e,
                    )

                except KeyboardInterrupt:
                    sys.exit("\nExiting the script...")

                except OSError as e:
                    print("Error with OS/path: ", e)

        case 2:
            print("In process....")
            print("Clear full directory")
            return True


        case 3:
            print("In process....")
            print("Clear full vault")
            return True
