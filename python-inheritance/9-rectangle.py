#!/usr/bin/python3
"""This module is the follow up"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """This class is a child"""
    def __init__(self, width, height):
        #  validates height & width
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        #  set private attributes for width & height
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"<name> must be an integer")
        if value <= 0:
            raise ValueError(f"<name> must be greater than 0")
