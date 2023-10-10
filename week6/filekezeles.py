def main():
    f = open("szoveg.txt", "r")  # [filenév][r,w,a] (read, write, append)
    for line in f:
        # print(line) # hagy '\n'-t
        # print(line, end='') # normálisan írja ki
        line = line.rstrip("\n")  # lstrip - balról , rstrip - jobbról
        print(line)
    f.close()


if __name__ == '__main__':
    main()
