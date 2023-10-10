PI = 3.14159

counter = 0


def f1():
    counter = 5
    print("F1 counter:", counter)


def f2():
    global counter
    counter = 42
    # print("F2 counter", counter)


def main():
    print("PI: ", PI)
    print("Counter:", counter)
    f1()
    f2()
    print("Counter after f():", counter)


if __name__ == '__main__':
    main()
