#!/usr/bin/python3
"""This function returns a json representation """
#  imports python's built-in module(JSON)

import json

def to_json_string(my_obj):
    """This function returns a json representation"""
    # json.dump creates a object and writes it directly into a file
    return json.dumps(my_obj)