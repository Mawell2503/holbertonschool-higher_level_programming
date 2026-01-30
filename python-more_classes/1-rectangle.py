#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle:
    """This class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """This method creates a private instance attribute width """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This methods works in pair with property as its value setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This methods works in pair with property as its value setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
    
        self.__height = value
