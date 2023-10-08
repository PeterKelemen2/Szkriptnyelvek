def calculate_result(base, exp):
    """
        Calculate and print the result of raising a base to an exponent.

        This function calculates the result of raising a given 'base' to a given
        'exp' (exponent) and then calculates the sum of the digits in the resulting
        number. It prints both the original calculation and the result.

        Args:
            base (int): The base value.
            exp (int): The exponent value.

        Returns:
            None: This function does not return a value. It prints the original
            calculation and the result to the console.
    """
    int_res = base ** exp
    str_res = str(int_res)
    num_list = [int(c) for c in str_res]

    res = 0
    for i in range(len(num_list)):
        res += num_list[i]

    print("\n" + str(base) + "^" + str(exp) + " = " + str(int_res) +
          "; \n  Result = " + str(res))


def main():
    """
        Main function to demonstrate the 'calculate_result' function with different
        exponent values.
    """
    calculate_result(2, 15)
    calculate_result(2, 1000)


if __name__ == "__main__":
    main()
