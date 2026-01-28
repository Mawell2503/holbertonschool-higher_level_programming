#!/usr/bin/python3
"""This code is to compute the square area"""


class Square:
    """This class is to know if size is usable"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This code squares square"""
        #  return a squared value
        return self.__size ** 2
