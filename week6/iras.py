import sys


def main():
    f = open("szoveg2.txt", "w")

    f.write("1")
    f.write("2")
    f.write("3")
    # ilyenkor nincs sortörés

    f.write("4\n")
    f.write("5\n")

    print("4", file=f)  # alapból van sortörés
    print("asdasdsd", file=sys.stdout)  # konzolra
    print("error", file=sys.stderr)  # piros
    f.close()


if __name__ == '__main__':
    main()
