def loop(num, debug=False):
    """
        Print numbers from 1 to 'num' in a space-separated string format.

        This function generates a space-separated string containing numbers from 1 to
        'num'. If the 'debug' parameter is set to True, it also prints debug comments
        before and after the loop execution.

        Args:
            num (int): The upper limit for generating numbers.
            debug (bool, optional): If True, print debug comments. Defaults to False.

        Returns:
            None: This function does not return a value. It prints the generated string.
    """
    if debug:
        print("\n# ciklus kezdete")

    res = ''
    for i in range(1, num + 1):
        res += str(i) + " "

    print(res)

    if debug:
        print("# ciklus vége")


def main():
    """
        Main function to demonstrate the 'loop' function with different 'num' values
        and debug modes.
    """
    loop(5)
    loop(6, True)


if __name__ == "__main__":
    main()
