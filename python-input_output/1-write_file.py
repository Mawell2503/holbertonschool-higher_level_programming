#!/usr/bin/python3

"""This module contains the function write_file."""


def write_file(filename="", text=""):
    """Write & returns number of characters written"""
    #  open "filename" on overwrite mode and convert characters > bytes
    #  "w" >> write mode/ovewrite file
    #  + link this to my_f
    with open(filename, "w", encoding="utf-8") as my_f:
        return my_f.write(text)
