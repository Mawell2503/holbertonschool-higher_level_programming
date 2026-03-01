#!/usr/bin/python3
"""This module defines a rectangle"""

class Rectangle:
    """Defines a rectangle"""
    #  the public attribute of the class
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width = 0, height = 0):
        """This module creates private instance attribute"""
        self.width = width
        self.height = height
        #  tracks how many times object(s) Rectangle created
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This module retrieves width"""
        return self.__width
    
    @width.setter
    def width(self,value):
        """This module is to set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This module retieves height"""
        return self.__height
    
    @height.setter
    def height(self,value):
        """This module is to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This module finds the area of rectangle"""
        return self.__width * self.__height
    
    def perimeter(self):
        """This module finds the perimeter of rectangle"""
        if (self.__width == 0 or
        self.__height == 0
        ):
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """This modules print."""
        if self.width == 0 or self.height == 0:
            return ""
        line = str(self.print_symbol) * self.width
        return "\n".join(line for _ in range(self.height))

    def __repr__(self):
        """Return string to recreate a new instance with eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """this method deletes the Rectangle"""
        #  deletes object(s) Rectangle when finished with it
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """This module checks for the rectangle with the bigger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError ("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
        
    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance where width == height == size."""
        return cls(size, size)
    
 