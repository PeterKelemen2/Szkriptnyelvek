class Sor:
    def __init__(self):
        self.s_list = []

    def __str__(self):
        elements = "["
        for i in range(len(self.s_list)):
            elements += (str(self.s_list[i]) + " ")
        return elements

    def ures(self):
        if len(self.s_list) == 0:
            return True
        else:
            return False

    def meret(self):
        return len(self.s_list)

    def betesz(self, item):
        self.s_list.append(item)

    def kivesz(self):
        if len(self.s_list) == 0:
            return None
        else:
            popped = self.s_list[0]
            self.s_list.pop(0)
            return popped


def main():
    sor = Sor()
    print(sor)
    print(sor.ures())
    sor.betesz(1)
    sor.betesz(2)
    sor.betesz(3)
    print(sor)
    print(sor.ures())
    print("Sor mérete: " + str(sor.meret()))
    sor.kivesz()
    print(sor)
    x = sor.kivesz()
    print("x = " + str(x))
    print(sor)
    sor.kivesz()
    print(sor)
    print(sor.ures())


if __name__ == "__main__":
    main()
