from .automation_one_file import comment_the_file
from pathlib import Path
import sys

def redirect_script(option):
    match option:
        case 1:
            while True:
                try:
                    path_input = input("Pass me the full path (with file): ")
                    path_input = path_input.strip("'\"")
                    path_input = Path(path_input)

                    if path_input.exists() and path_input.is_file():  
                        comment_the_file(path_input)
                        break
                    else:
                        print("Pass the correct path (or exit Ctrl + C)...")

                except Exception as e:
                    print("Error with the input path (check the file, directory, full path...): ", e)

                except KeyboardInterrupt:
                    sys.exit("\nExiting the script...")

        case 2:
            print("Clear full directory")

        case 3:
            print("Clear full vault")