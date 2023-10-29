def main():
    aux_list = []
    checksum = 0

    file = open("table.txt", "r")
    text = file.read().splitlines()
    for line in text:
        line = line.split()
        for c in line:
            aux_list.append(int(c))
        print("Current line: " + str(aux_list))

        checksum += max(aux_list) - min(aux_list)
        aux_list = []

    file.close()
    print(checksum)


if __name__ == "__main__":
    main()
