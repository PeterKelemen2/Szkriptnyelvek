def diamond(height):
    s = ""
    print("Magasság: " + str(height))
    for i in range(1, height):
        if i % 2 != 0:
            aux = "*" * i
            aux = aux.center(height, " ")
            # s += "\n" + "*" * i
            s += "\n" + aux

    s_rev = ''.join(reversed(s))
    s_middle = "*" * height
    s_res = s + "\n" + s_middle + "\n" + s_rev
    print(s_res)


def main():
    x = 0
    is_good = False
    while not is_good:
        x = int(input("Írj egy számot: "))
        if x % 2 != 0:
            is_good = True
            print()
        else:
            print("Nem jó a szám!")

    diamond(x)


if __name__ == "__main__":
    main()
