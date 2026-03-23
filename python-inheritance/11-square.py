#!/usr/bin/python3
import "9-rectangle.py"

"""This module defines a square"""


class Square:
    def __init__(self, size, height, width, length):
        self.__size = size
        self.width = width
        self.height = height
        self.length = length
    
    def area(self):
        return self.width * self.height
    
    def integer_validator(self, value):
        if type(value) is not in:

