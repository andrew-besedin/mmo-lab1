import math


class Figure:
    def area(self):
        return 0


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def main():
    radius = float(input("Enter circle radius: "))
    side = float(input("Enter square side: "))
    width, height = map(float, input("Enter rectangle width and height: ").split())
    figures = [Circle(radius), Square(side), Rectangle(width, height)]
    for figure in figures:
        print(type(figure).__name__, "area:", figure.area())


main()
