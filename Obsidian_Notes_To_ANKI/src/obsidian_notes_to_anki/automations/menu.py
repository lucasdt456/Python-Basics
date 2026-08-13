import logging
import sys

logger = logging.getLogger(__name__)


def menu() -> int:
    print("=========== Select an option ============")
    print("|    1. Clear only 1 file (quickly)     |")
    print("|    2. Clear full directory (extense)  |")
    print("|    3. Clear full vault (very extense) |")
    print("=========================================")
    print("============ Exit (Ctrl + C) ============")

    while True:
        try:
            option = int(input("Your option: "))

            if 1 <= option <= 3:
                logger.info(f"The user selected a good option: {option}")
                return option
            else:
                logger.warning("Select a good option (range 1-3)")

        except ValueError:
            logger.warning("Insert a number (range 1 - 3)")

        except KeyboardInterrupt:
            logger.info("(Ctrl + C): Exiting the script...")
            sys.exit(0)

        # except Exception as e:
        #     logger.exception("Unexpected General Error occurred in menu.")
        #     sys.exit(1)
