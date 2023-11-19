#!/usr/bin/env python

# Polymorphism: overriding 关于方法的重载性
class BaseShape(object):
    def __init__(self):
        self.name = "shape"

    def print_name(self):
        print("The name is BaseShape")


class Circle(BaseShape):
    def __init__(self):
        super().__init__()
        self.name = "Circle"

    def print_name(self):
        print("The name is Circle")


class Rectangle(BaseShape):
    def __init__(self):
        super().__init__()
        self.name = "Rectangle"

    def print_name(self):
        print("The name is Rectangle")


if __name__ == "__main__":
    base = BaseShape()
    circle = Circle()
    rectangle = Rectangle()

    base.print_name()
    circle.print_name()
    rectangle.print_name()

