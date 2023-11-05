def to_binary(num: int):
    return int(bin(num)[2:])


def is_palindrome(param: int):
    if str(param) == str(param)[::-1]:
        return True
    return False


def sum_up_to(ceil: int):
    palindrome_sum = 0
    for num in range(0, ceil):
        # It can't be palindrome is the last number or character is 0
        if num % 10 != 0 or to_binary(num) % 10 == 0:
            # If they are both palindromes, the decimal value is added to the sum
            if is_palindrome(num) and is_palindrome(to_binary(num)):
                palindrome_sum += num
                print(num, '-', to_binary(num))

    print("Sum =", palindrome_sum)
    return palindrome_sum


def main():
    sum_up_to(1000000)


if __name__ == "__main__":
    main()
