#!/usr/bin/python3
"""This is a file  """


#  filename="" is basically a variable for the file u will input

def read_file(filename=""):
    """Reads a utf-8 text fie and prnts it"""
    #  open > built in function that open a file
    #  encoding="utf-8" > translate the content of the file to character
    #  utf-8 > character encoding system
    #  as f > basically n likimama handle
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
