import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def exists(self):
        a = self.a
        b = self.b
        c = self.c
        return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


def main():
    a, b, c = map(float, input("Enter three sides: ").split())
    triangle = Triangle(a, b, c)
    if triangle.exists():
        print("Triangle exists")
        print("Area:", triangle.area())
        print("Perimeter:", triangle.perimeter())
    else:
        print("Triangle does not exist")


main()
