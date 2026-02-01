#!/usr/bin/python3
"""This module defines a Rectangle"""


class Rectangle:
    """This class is a Rectangle"""
    def __init__(self, width=0, height=0):
        """This module creates a private instance attribute"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This module is to retrieve width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """This module is to set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width > 0:
            raise ValueError("width must be >= 0")
        
    @property
    def height(self):
        """This module is to retrieve height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """This module is to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height musr be ann integer")
        if height < 0:
            raise (ValueError(" heigh must be >= 0"))