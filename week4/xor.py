str1 = "python"
str2 = None


def main():
    print("bool(str1): " + str(bool(str1)))
    print("bool(str2): " + str(bool(str2)))

    if bool(str1) and not bool(str2):
        print("A feltevés helyes volt")


if __name__ == "__main__":
    main()
