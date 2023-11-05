def user_input_pages():
    user_input = input("Please type in the pages you'd like to print: ")
    pages_input = user_input.strip().split(',')
    print("Input was: ", pages_input)

    for elem in pages_input:
        if check_for_invalid_chars(elem):
            pages_input.remove(elem)

    return pages_input


def check_for_invalid_chars(elem: str):
    if elem.lower() != elem.upper():
        print("Found invalid page: ", elem)
        return True
    return False


def extract_pages_from_interval(param: str):
    result = []

    front = int(param[:param.index('-')])
    print("Front of '-' : ", front)

    back = int(param[param.index('-') + 1:])
    print("Back of '-' : ", back)

    for i in range(front, back + 1):
        result.append(int(i))

    return result


def pages_to_print(param=None):
    pages_output = []

    if param is None:
        # Making the user type in the pages
        pages_input = user_input_pages()

        for elem in pages_input:
            # This checks if there are chars beside numbers
            if check_for_invalid_chars(elem):
                pages_input.remove(elem)

        for elem in pages_input:
            if '-' in elem:
                pages_output += (extract_pages_from_interval(elem))
            else:
                pages_output.append(int(elem))
    else:
        pages_input = param.strip().split(',')
        print("Input: ", pages_input)
        for elem in pages_input:
            if '-' in elem:
                pages_output += (extract_pages_from_interval(elem))
            else:
                pages_output.append(int(elem))

    print("Page(s) to print: ", sorted(pages_output))


def main():
    print("Pages given as parameter:")
    pages_to_print("1-4,7,9,11-    15")

    print("\nNo parameter given:")
    pages_to_print()


if __name__ == "__main__":
    main()
