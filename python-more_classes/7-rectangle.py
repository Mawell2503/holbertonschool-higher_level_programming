#!/usr/bin/python3
"""This module defines a Rectangle"""


class Rectangle:
    """This class is a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This module creates a private instance attribute"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This module is to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This module is to set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This module is to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This module is to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise (ValueError("height must be >= 0"))
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        line = []
        for i in range(self.__height):
            line.append(str(self.print_symbol) * self.width)
        return "\n" .join(line)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
