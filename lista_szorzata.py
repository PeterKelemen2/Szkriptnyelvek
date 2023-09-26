numbers = [1, 2, 3, 4, 5]
res = 0


def szorzat_of(list):
    res = 1
    for i in range(0, len(list) - 1):
        res = res * list[i]
    return res


def main():
    print(szorzat_of(numbers))


if __name__ == "__main__":
    main()
