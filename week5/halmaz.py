def feladat1():
    aux = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    print(sorted(set(aux)))


def main():
    kosar = ['banan', 'banan', 'alma', 'oszibarack']
    # print(kosar)
    gyumolcsok = set(kosar)
    # print(gyumolcsok)

    # print(sorted(gyumolcsok))
    # print("banan" in gyumolcsok)
    # print("málna" in gyumolcsok)

    # feladat1()

    a = set(["banan", "alma"])
    print(gyumolcsok)
    print(a)

    print(gyumolcsok.union(a))
    print(gyumolcsok.difference(a))
    print(gyumolcsok.intersection(a))


if __name__ == '__main__':
    main()
