#!/usr/bin/python3
from base_geometry import BaseGeometry
"""This module is the follow up"""


class Rectangle(BaseGeometry):
    """This class is a child"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
