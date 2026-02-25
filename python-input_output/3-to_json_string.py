#!/usr/bin/python3
#  imports python's built-in module(JSON)
import json

"""This function returns a json representation """
def to_json_string(my_obj):
    """This function returns a json representation"""
    # json.dump creates a object and writes it directly into a file
    return json.dumps(my_obj)