def negyzetosszeg(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result


def osszegenek_a_negyzete(n):
    result = ((n * (n + 1)) // 2) ** 2
    return result


def kulonbseg_of_osszn_nossz(n):
    print(str(n) + ": " + str(osszegenek_a_negyzete(n) - negyzetosszeg(n)))
    return osszegenek_a_negyzete(n) - negyzetosszeg(n)


def main():
    kulonbseg_of_osszn_nossz(10)  # 2640 a példa szerint
    kulonbseg_of_osszn_nossz(100)


if __name__ == "__main__":
    main()
