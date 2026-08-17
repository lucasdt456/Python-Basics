import logging
import sys
from pathlib import Path

from .automation_directory import comment_one_directory
from .automation_one_file import comment_the_file

logger = logging.getLogger(__name__)


def redirect_script(option):
    match option:
        case 1:
            print("You selected the option 1: Clear only 1 file (quickly)")
            return chase_option(option)

        case 2:
            print("You selected the option 2: Clear an entire directory (extense)")
            return chase_option(option)

        case 3:
            print("You selected the option 3: Clear a full vault (very extense)")
            return chase_option(option)


def chase_option(option_selected):

    config = {
        1: {
            "prompt": "Pass me the full path (with file): ",
            "validator": lambda p: p.is_file(),
            "action": comment_the_file,
        },
        2: {
            "prompt": "Pass me the full path (without file): ",
            "validator": lambda p: p.is_dir(),
            "action": comment_one_directory,
        },
        3: {
            "prompt": "Pass me the initial path (root of the vault): ",
            "validator": lambda p: p.is_dir(),
            "action": comment_one_directory,
        },
    }

    current_config = config.get(option_selected)

    if not current_config:
        return

    while True:
        try:
            path_input = input(current_config["prompt"])
            path_input = path_input.strip().strip("'\"").replace(r"\ ", " ")
            path_input = Path(path_input)

            if path_input.exists() and current_config["validator"](path_input):
                logger.debug(f"User provided a valid path: {path_input}")
                current_config["action"](path_input)
                return True

            else:
                logger.debug(f"User provided an invalid path: {path_input}")
                print("Pass the correct path (or exit Ctrl + C)...")

        except KeyboardInterrupt:
            print("\n(Ctrl + C): Exiting the script...")
            logger.info("(Ctrl + C): Exiting the script...")
            sys.exit(0)

        except OSError:
            logger.exception("Error with OS/path")
            sys.exit(1)

        except (PermissionError, FileNotFoundError):
            logger.exception("Error with path/file (not found or not permission)")
            sys.exit(1)

        # except Exception:
        #     logger.exception(
        #         "Error with the input path (check the file, directory, full path...)"
        #     )
        #     sys.exit(1)
