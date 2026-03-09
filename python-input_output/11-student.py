#!/usr/bin/python3
"""This module defines a Student"""


class Student:
    """This is a student class"""
    def __init__(self, first_name, last_name, age):
        """This module identify students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This module retrieves instances of a dictionary"""
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attr):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__
    
    def reload_from_json(self, json):
        """This module replaces attributes"""
        for key, value in json.items():
            setattr(self, key, value)
