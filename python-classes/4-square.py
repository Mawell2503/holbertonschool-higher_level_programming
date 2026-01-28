#!/usr/bin/python3
"""This code is to compute the square area"""


class Square:
    """This class defines a square"""

    #  value of size is now in instance size in attribute self
    def __init__(self, size):
        self.size = size 

    #  return size without exposing or reaking it
    @size.property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This block is a size setter"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This code squares size"""
        return self.__size ** 2
