#!/usr/bin/python3
"""This module is something ig"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class"""
    #  checks if object is subclass OF class a_class or is an instance
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
