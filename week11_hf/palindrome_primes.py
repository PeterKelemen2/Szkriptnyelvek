import json


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False


def main():
    f = open("primes.json", "r")
    primes_list = json.load(f)

    num_of_pal_primes = 0

    for i in range(0, len(primes_list)):
        if is_palindrome(primes_list[i]):
            num_of_pal_primes += 1

    print("Number of palindrome primes: ", num_of_pal_primes)


if __name__ == "__main__":
    main()
