#!/usr/bin/python3
"""This module is something ig"""


def is_kind_of_class(obj, a_class):
    """This function is sbhtsnrdbr"""
    #  checks if object is subclass OF class a_class or is an instance
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
