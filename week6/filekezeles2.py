def main():
    f = open("szoveg.txt", "r")  # [filenév][r,w,a] (read, write, append)

    lines = f.readlines()  # listát ad vissza
    print(lines)

    f.close()


if __name__ == '__main__':
    main()
