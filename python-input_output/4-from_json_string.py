#!/usr/bin/python3
"""Module that provides a function to convert a JSON string to a python object"""

import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string."""
    #  json.loads is used to read JSON data from a file and convert it into a Python object
    #  JSON string > Python
    return json.loads(my_str)
