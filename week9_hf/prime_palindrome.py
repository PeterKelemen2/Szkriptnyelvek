def is_prime(num: int):
    # The first 3 primes are easier to test like this
    if 1 <= num <= 3:
        return True

    # Primes are not even
    if num % 2 == 0:
        return False

    # Previous cases were already tested and 4 is not a prime, so this starts from 5
    for i in range(5, num // 2):
        if num % i == 0:
            return False

    # In every other case
    return True


def is_palindrome(param: int):
    if str(param) == str(param)[::-1]:
        return True
    return False


def print_next_palindrome_prime(num: int):
    if is_palindrome(num) and is_prime(num):
        # This number is him
        print("Next palindrome prime of (" + str(num) + "): " + str(num))
        return

    for i in range(num, num * 1000):
        if is_palindrome(i):
            if is_prime(i):
                print("Next palindrome prime of (" + str(num) + "): " + str(i))
                return


def main():
    print_next_palindrome_prime(31)
    print_next_palindrome_prime(130)
    print_next_palindrome_prime(131)
    print_next_palindrome_prime(1977)


if __name__ == "__main__":
    main()
