# import os
import logging
from pathlib import Path

from .automation_one_file import comment_the_file

logger = logging.getLogger(__name__)


def comment_one_directory(full_path: Path) -> int:

    directory = Path(full_path).glob("**/*.md")
    count = 0
    try:
        for f in directory:
            file = comment_the_file(f)
            if isinstance(file, Path):
                count += 1

        print("==========================")
        print("|                        |")
        print(f" Total files cleared: {count}  ")
        print("|                        |")
        print("==========================")
        return count

    except Exception:
        logger.critical("Critical error in recursive cleaning", exc_info=True)
        return count
