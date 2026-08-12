import sys
import logging
from pathlib import Path
from .automation_one_file import comment_the_file

logger = logging.getLogger(__name__)

def redirect_script(option):
    match option:
        case 1:
            print("You selected the option 1: Clear only 1 file (quickly)")

            while True:
                try:
                    path_input = input("Pass me the full path (with file): ")
                    path_input = path_input.strip("'\"")
                    path_input = Path(path_input)

                    if path_input.exists() and path_input.is_file():
                        logger.debug(f"User provided a valid path: {path_input}")
                        comment_the_file(path_input)
                        return True
                    else:
                        logger.debug(f"User provided an invalid path: {path_input}")
                        print("Pass the correct path (or exit Ctrl + C)...")

                except KeyboardInterrupt:
                    logger.info("(Ctrl + C): Exiting the script...")
                    sys.exit(0)

                except OSError:
                    logger.exception("Error with OS/path")
                    sys.exit(1)

                except Exception:
                    logger.exception(
                        "Error with the input path (check the file, directory, full path...)"
                    )
                    sys.exit(1)

        case 2:
            print("In process....")
            print("Clear full directory")
            return True


        case 3:
            print("In process....")
            print("Clear full vault")
            return True
