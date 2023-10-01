def gauss(n):
    return ((n + 1) * n) // 2


def main():
    result = 0
    sum = gauss(100)
    sum_list = list(str(sum))

    for i in range(len(sum_list)):
        result += int(sum_list[i])

    print(result)  # Variáció


if __name__ == "__main__":
    main()
