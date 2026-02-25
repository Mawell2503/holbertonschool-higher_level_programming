#!/usr/bin/python3
"""Module returns an object"""

import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string."""
    #  json.loads: read JSON data and convert it into a Python object
    #  JSON string > Python
    return json.loads(my_str)
