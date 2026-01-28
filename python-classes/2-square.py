#!/usr/bin/python3
"""This code defines a Square class"""


class Square:
    """this class checks what size is and makes it a private instance"""
    def __init__(self, size=0):
        #  check if size is int
        if not isinstance(size, int):   
            raise TypeError("size must be an integer")
        #  check if size is greater than 0 
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
