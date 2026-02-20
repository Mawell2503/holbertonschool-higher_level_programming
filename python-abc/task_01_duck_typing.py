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
        self.check_radius(radius)
        self.radius = radius

    def check_radius(self, value):
        self.radius = value
        if not isinstance(value, int):
            raise TypeError("radius must be an integer")
        if value < 0:
            raise ValueError("radius is negative")
        
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi *self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.check_width(width)
        self.check_height(height)
        self.width = width
        self.height = height

    def check_width(self, value):
        self.width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width is negative")
        
    def check_height(self, value):
        self.height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height is negative")
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(Shape):
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
    
