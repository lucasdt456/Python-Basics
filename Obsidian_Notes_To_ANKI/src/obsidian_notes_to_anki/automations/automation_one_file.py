# import os
import sys
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

TEXT_TO_SEARCH = "TARGET DECK"

def comment_the_file(full_path: Path) -> Path | bool:
    find = False
    
    if full_path.exists() and full_path.is_file():
        content = full_path.read_text(encoding="utf-8")

        if not content:
            print(f"The file '{full_path.name}' is empty.")
            return False

        lines = content.splitlines(keepends=True)

        for line in lines:
            if "!These are annotated¡" in line:
                print(
                    f"This file: '{full_path.name}' has been modified previously "
                    f"(contains the comment to disable the note) in this path: '{full_path}'"
                )
                print("Skipping this file...")
                logger.debug(f"The file '{full_path.name}' was not modified (it has already been modified previously)")
                return False

        try:
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
                    
        except IndexError:
            logger.critical("Error indexing the file content during the search", exc_info=True)
            raise 

        if find:
            content = "".join(lines)
            full_path.write_text(content)
            print("The changes are correct.")
            print("Exiting the script...")
            logger.debug(f"Correct changes in '{full_path.name}' file")
            return full_path

        else:
            print(
                f"This file: '{full_path.name}' is not a note (ANKI <-> Obsidian) "
                f"or does not contain '{TEXT_TO_SEARCH}'."
            )
            logger.debug(f"The file '{full_path.name}' is not a note")
            return False
            
    else:
        print(f"This path: '{full_path}' doesn't exist or is not a valid file.")
        logger.debug(f"Invalid file '{full_path.name}' or path '{full_path}'")
        return False