import sys
import random as r

UPTO = 100


def main():
    for i in range(UPTO):
        if i % (10 + 1) == 0:
            print()
        else:
            print(r.randint(0, 9), end="")

    print()


if __name__ == "__main__":
    main()
