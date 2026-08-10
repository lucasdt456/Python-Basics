import sys

def menu() -> int:
    print("=========== Select an option ============")
    print("|    1. Clear only 1 file (quickly)     |")
    print("|    2. Clear full directory (extense)  |")
    print("|    3. Clear full vault (very extense) |")
    print("=========================================")

    while True:
        try:
            option = int(input("You're option: "))

            if 1 <= option <= 3:
                return option

            else:
                print("Select a good option (range 1-3) or exit (Ctrl + C)")

        except ValueError as e:
            print("Insert a number (range 1 - 3)", e)

        except KeyboardInterrupt:
            sys.exit("\nExiting the script...")

        except Exception as e:
            print("General Error: ", e)
            return
