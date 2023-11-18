from math import sqrt

import json


def generate_primes_up_to(n):
    primes_list = []
    lst = [True] * n
    for i in range(2, int(sqrt(n)) + 1):
        if lst[i]:
            for j in range(i * i, n, i):
                lst[j] = False

    for i in range(2, n):
        if lst[i]:
            primes_list.append(i)
            print(i)

    return primes_list


def main():
    primes_list = generate_primes_up_to(10000000)

    f = open("primes.json", "w")
    json.dump(primes_list, f, indent=4)
    f.close()


if __name__ == "__main__":
    main()
