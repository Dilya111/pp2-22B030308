class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0


class Square(Shape):
    def area(self):
        return self.length**2

first = Square(3)
print(first.area())
second = Square(33)
print(second.area())
third = Shape(10)
print(third.area())