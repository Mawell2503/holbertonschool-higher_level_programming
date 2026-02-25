#!/usr/bin/python3
"""Writes an Object to a txt.file"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a txt.file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
