def calculate(num):
    """
        Calculate the sum of consecutive digits in a given integer.

        This function takes an integer 'num', converts it to a string, and then
        calculates the sum of consecutive digits that are the same, treating the
        integer as a circular list (i.e., the last digit is considered consecutive
        to the first if they are the same).

        Args:
            num (int): The integer to be analyzed.

        Returns:
            None: This function does not return a value. It prints the calculated
            result to the console.
    """
    str_num = str(num)
    nums = [int(c) for c in str_num]
    nums.append(nums[0])
    print(nums[:-1])

    count = 1
    result = 0
    for i in range(len(nums) - 1):
        # print(str(nums[i]) + " - " + str(nums[i + 1]))
        if nums[i] == nums[i + 1]:
            result += nums[i]

    print("result: " + str(result))
    print()


def main():
    """
        Main function to demonstrate the 'calculate' function with different integers.
    """
    calculate(1122)
    calculate(1111)
    calculate(1234)
    calculate(91212129)


if __name__ == "__main__":
    main()
