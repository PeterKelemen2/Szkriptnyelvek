import sys

accepted = ["y", "yes", "Y"]

def main():
    inp = input("Do you really want to quit [y/Y/yes]? ")
    if inp in accepted:  # <- egyszerűbben?
        print('bye')
        sys.exit(0)
    # for any other input:
    print('The show goes on...')


if __name__ == "__main__":
    main()
