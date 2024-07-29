from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self, *args):
        pass


class Circle(Shape):
    def area(self, radius):
        s = pi * radius ** 2
        return round(s, 2)


class Rectangle(Shape):
    def area(self, length, width):
        s = length * width
        return round(s, 2)


class Triangle(Shape):
    def area(self, length, height):
        s = 0.5 * length * height
        return round(s, 2)


circle = Circle()
rect = Rectangle()
triangle = Triangle()

print(circle.area(30))
print(rect.area(10, 40))
print(triangle.area(40, 10))
