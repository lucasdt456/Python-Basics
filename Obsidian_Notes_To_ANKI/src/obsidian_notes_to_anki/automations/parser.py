import argparse

# import logging


def parse_arguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="Pass a parser")
    parser.add_argument(
        "-o",
        "--option",
        type=int,
        choices=[1, 2, 3],
        help="Select option (1 = clear one file; "
        "2 = clear one directory; 3 = clear full vault)",
    )
    # logging.debug(f"Parse arguments function finish. With option:
    # {parser.parse_args().option}")
    args = parser.parse_args()
    return args
