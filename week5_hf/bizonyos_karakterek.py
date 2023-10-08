def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    Filter characters in the input text based on the provided character set.

    Args:
        text (str): The input text that needs to be filtered.
        chars (str, optional): The character set used for filtering. Defaults to
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".

    Returns:
        str: A new string containing only characters from the input text that are
             present in the specified character set.
    """
    res = ""
    for c in range(len(text)):
        if text[c] in chars:
            res += text[c]
    print('"' + str(res) + '"')
    return res


def main():
    """
    Main function to demonstrate the 'valid' function with different character sets.
    """
    valid("Barking!")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")


if __name__ == "__main__":
    main()
