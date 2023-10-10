def main():
    f = open("szoveg.txt", "r")  # [filenév][r,w,a] (read, write, append)

    # text = f.read()  # simán stringbe építi
    text = f.read().splitlines()  # vagy split("\n")
    print(text)

    f.close()


if __name__ == '__main__':
    main()
