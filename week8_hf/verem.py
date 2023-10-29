class Verem:
    def __init__(self):
        self.v_list = []

    def __str__(self):
        elements = "["
        for i in range(len(self.v_list)):
            elements += (str(self.v_list[i]) + " ")
        return elements

    def ures(self):
        if len(self.v_list) == 0:
            return True
        else:
            return False

    def meret(self):
        return len(self.v_list)

    def betesz(self, item):
        self.v_list.append(item)

    def kivesz(self):
        if len(self.v_list) == 0:
            return None
        else:
            popped = self.v_list[len(self.v_list) - 1]
            self.v_list.pop(len(self.v_list) - 1)
            return popped


def main():
    v = Verem()
    print(v)
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)


if __name__ == "__main__":
    main()
