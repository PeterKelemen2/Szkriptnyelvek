import sys


def main():
    if len(sys.argv) != 2:
        print("Hiba! Meg kell adni egy(!) darab parancssori argumentumot a működéshez", file=sys.stderr)
        sys.exit(1)  # Hibakóddal terminál
    elif len(sys.argv[1]) < 10:
        print("Hiba! A megadott parancssori argumentum túl rövid", file=sys.stderr)
        sys.exit(2)
    elif len(sys.argv[1]) > 10:
        print("Hiba! A megadott parancssori argumentum túl hosszú", file=sys.stderr)
        sys.exit(3)

    chars = list(sys.argv[1])
    paros_ascii = [int(ord(c) * 1.5) for c in chars if ord(c) % 2 == 0]
    paratlan_ascii = [ord(c) * -2 for c in chars if ord(c) % 2 == 1]

    print(paros_ascii)
    print(paratlan_ascii)

    res = paros_ascii + paratlan_ascii
    print(res)
    return res


if __name__ == '__main__':
    main()
