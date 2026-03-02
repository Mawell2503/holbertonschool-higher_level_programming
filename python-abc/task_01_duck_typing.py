#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be an integer")
        #  abs is a built-in function that means absolute value
        #  means: make the number positive
        self.radius = abs(radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi *self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
