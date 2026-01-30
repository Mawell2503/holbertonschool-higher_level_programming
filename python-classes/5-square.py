#!/usr/bin/python3
"""This code prints a sqaure"""


class Square:
    """Defines a square"""


    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrives size"""
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
        """Squares"""
        return self.__size **2
    
    def my_print(self):
        """Prints square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                    print("#" * self.__size)

