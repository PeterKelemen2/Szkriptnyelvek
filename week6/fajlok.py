def make_copy(source, to):
    file_from = open(source, "r")
    file_to = open(to, "w")
    for line in file_from:
        file_to.write(line)

    file_from.close()
    file_to.close()


def main():
    with open("szoveg.txt", "r") as f:
        print(f.read())

    make_copy("szoveg.txt", "szoveg2.txt")
    

if __name__ == '__main__':
    main()
