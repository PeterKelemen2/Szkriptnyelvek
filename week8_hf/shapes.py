import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "Sphere (radius = {r})".format(r=self.radius)

    def __bool__(self):
        return self.volume() > 0

    def __lt__(self, other):
        return self.volume() < other.volume()

    def surfaceArea(self):
        return 4 * math.pi * self.radius * self.radius

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def __str__(self):
        return "Ellipse with parameters of {ma_a}, {mi_a}".format(ma_a=self.major_axis,
                                                                  mi_a=self.minor_axis)

    def __bool__(self):
        return self.area() > 0

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def area(self):
        return self.major_axis * self.minor_axis * math.pi


def main():
    sphere = Sphere(7)
    sphere2 = Sphere(10)
    print(sphere)
    print("Sphere surface area: " + str(sphere.surfaceArea()))
    print("Sphere volume: " + str(sphere.volume()))
    print(sphere < sphere2)

    print()

    ellipse = Ellipse(5, 3)
    ellipse2 = Ellipse(5, 3)
    print(ellipse)
    print("Ellipse area: " + str(ellipse.area()))
    print(ellipse < ellipse2)
    print(ellipse <= ellipse2)


if __name__ == "__main__":
    main()
