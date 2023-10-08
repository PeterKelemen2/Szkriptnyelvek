def print_table(arr):
    """
    Prints a formatted chessboard table based on the provided 2D array.

    Args:
        arr (list): A 2D list representing the chessboard layout.

    Returns:
        None: This function does not return a value. It prints the formatted table directly.
    """
    arr = correct_format(arr)
    res = ""
    print(" + " + " - " * 8 + " +")
    for i in range(8):
        if i != 0:
            res += '\n | '
        else:
            res += " | "
        for j in range(8):
            res += str(arr[i][j])
            if j == 7:
                res += " | "
    print(res)
    print(" + " + " - " * 8 + " +\n")


def correct_format(arr2):
    """
    Transposes and reverses the provided 2D array.

    Args:
        arr2 (list): A 2D list representing a chessboard layout.

    Returns:
        list: A new 2D list with rows and columns swapped and reversed.
    """
    tp = list(zip(*arr2))
    tp = tp[::-1]
    return tp


def print_queens(queens):
    """
    Prints a chessboard with queens placed in their respective positions.

    Args:
        queens (list): A list of integers representing the column positions of queens.

    Returns:
        None: This function does not return a value. It prints the chessboard with queens.
    """
    table = []
    for i in range(8):
        a = []
        for j in range(8):
            a.append(' . ')
        table.append(a)

    for i in range(8):
        table[i][queens[i]] = ' Q '

    print_table(table)


def main():
    """
    Main function to demonstrate the placement of queens on a chessboard.
    """
    print_queens([7, 3, 0, 2, 5, 1, 6, 4])
    print_queens([0, 4, 7, 5, 2, 6, 1, 3])


if __name__ == "__main__":
    main()
