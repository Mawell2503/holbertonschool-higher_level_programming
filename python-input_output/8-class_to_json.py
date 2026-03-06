#!/usr/bin/python3
"""This module returns ditionary description"""


def class_to_json(obj):
    #  __dict__ contains all instances attribute
    return obj.__dict__
