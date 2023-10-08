def median(arr):
    """
        Calculate and print the median of a list of numbers.

        This function takes a list of numbers 'arr', sorts it in ascending order, and
        then calculates and prints the median value. If the list has an odd number of
        elements, the median is the middle element. If the list has an even number of
        elements, the median is the average of the two middle elements.

        Args:
            arr (list): A list of numbers for which the median needs to be calculated.

        Returns:
            None: This function does not return a value. It prints the calculated median
            to the console.
    """
    sorted_arr = sorted(arr)
    print(sorted_arr)
    if len(sorted_arr) % 2 != 0:
        print(sorted_arr[len(sorted_arr) // 2])
    else:
        a = sorted_arr[len(sorted_arr) // 2]
        b = sorted_arr[len(sorted_arr) // 2 - 1]
        print((a + b) / 2)


def main():
    """
        Main function to demonstrate the 'median' function with different lists of numbers.
    """
    median([1, 2, 3, 4, 5])
    median([3, 1, 2, 5, 3])
    median([1, 300, 2, 200, 1])
    median([3, 6, 20, 99, 10, 15])


if __name__ == "__main__":
    main()
