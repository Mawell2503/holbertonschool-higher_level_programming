#!/usr/bin/python3
"""This code is to compute the square area"""


class Square:
    """This class defines a square"""

    #  every def is a method

    #  stores value of size in the insatnance's attribute self.size
    def __init__(self, size=0):
        self.size = size

    #  return size without exposing or reaking it
    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This block is a size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This code squares size"""
        return self.__size ** 2
