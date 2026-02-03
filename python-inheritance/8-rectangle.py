#!/usr/bin/python3
"""This module is the follow up"""


#  Bring in the BaseGeometry class from its fie
from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """This class is a child"""
    def __init__(self, width, height):
        #  validates height & width
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        #  set private attributes for width & height
        self.__width = width
        self.__height = height
