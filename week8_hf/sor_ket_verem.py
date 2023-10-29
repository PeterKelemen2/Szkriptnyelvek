class MyQueue:
    def __init__(self):

        self.verem1 = []
        self.verem2 = []
        self.pop_from = 0
        self.verem_size = 0
        # print(verem1)
        # print(verem2)

    def __str__(self):
        res = "MyQueue: ["
        for i in range(0, len(self.verem2)):
            if self.verem2[i] != "":
                res += str(self.verem2[i]) + " "
        return res

    def append(self, to_add):
        self.verem1.append(to_add)
        self.verem2 = self.verem1

    def popleft(self):
        if self.pop_from < len(self.verem2):
            self.verem2[self.pop_from] = ""
            self.pop_from += 1

    def is_empty(self):
        if (self.size()) == 0:
            return True
        else:
            return False

    def size(self):
        self.verem_size = 0
        for i in range(len(self.verem2)):
            if self.verem2[i] != "":
                self.verem_size += 1
        return self.verem_size


def main():
    test = MyQueue()
    print("Is empty: " + str(test.is_empty()))
    test.append(1)
    test.append(2)
    test.append(3)
    test.append(4)
    print(test)
    print("Size: " + str(test.size()))
    test.popleft()
    test.append(5)
    print(test)
    test.popleft()
    print(test)
    print("Size: " + str(test.size()))
    print("Is empty: " + str(test.is_empty()))
    test.popleft()
    test.popleft()
    test.popleft()
    test.popleft()
    test.popleft()
    print("Is empty: " + str(test.is_empty()))


if __name__ == "__main__":
    main()
