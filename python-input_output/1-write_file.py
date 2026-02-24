#!/usr/bin/python3

"""This module contains the function write_file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns number of characters written"""
    #  open "filename" on overide mode and convert characters > bytes
    #  + link this to my_f
    with open(filename, "w", encoding="utf-8") as my_f:
        return my_f.write(text)