# Palindróm (1)
def palindrome_one():
    print("\n = Palindróm (1) =")
    check_pal = input("Enter a string: ")
    aux = check_pal[::-1]
    if (check_pal == aux):
        print(check_pal + " is palindrome")
    else:
        print(check_pal + " is not palindrome")


# Palindróm (2)
def palindrome_two():
    print("\n = Palindróm (2) =")
    check_pal_two = input("Enter a string: ")
    i = 0

    while (len(check_pal_two) >= 1):
        if check_pal_two[0] == check_pal_two[-1]:
            check_pal_two = check_pal_two[1:-1]
        else:
            print("Not palindrome")
            return

    print("Palindrome")


def palindrome_recursive(word):
    if len(word) <= 1:
        return True

    if word[0] == word[-1]:
        return palindrome_recursive(word[1:-1])
    else:
        return False


def palindrome_recursive_print(word):
    print("\n = Palindróm (3) =")
    if (palindrome_recursive(word)):
        print(word + " palindrome")
    else:
        print(word + " not palindrome")


palindrome_one()
palindrome_two()
palindrome_recursive_print("görög")
