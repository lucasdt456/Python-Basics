import argparse

def parse_arguments() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--option", type=int, choices=[1, 2, 3], help="Select option (1 = clear one file; 2 = clear one directory; 3 = clear full vault)")
    return parser.parse_args()

