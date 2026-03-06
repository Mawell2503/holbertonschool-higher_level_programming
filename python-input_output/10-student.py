#!/usr/bin/python3
"""This module defines a student class"""


class Student:
    """Class students"""

    def __init__(self, first_name, last_name, age):
        """Initialize students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    #  attrs > attributes
    def to_json(self, attrs=None):
        """Retrieves attributes of students"""
        #  if attribute is a list
        if isinstance(attrs, list):
            #  {} creates an empty dictionary 
            #  [] creates an empty list
            result = {}
            for attr in attrs:
                #  hasattr() is a Built In Python Function(BIPF)
                #  it checks if an object has a specific attribute
                #  if self is attr
                if hasattr(self, attr):
                    #  getattr() BIPF
                    #  it gets the value of an attribute from an obj
                    #  in result[] put the value u get when u check self
                    result[attr] = getattr(self, attr)
            #  return result
            return result
        return self.__dict__
