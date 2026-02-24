#!/usr/bin/python3
"""This module contains the function append_write."""

def append_write(filename="", text=""):
    """Appends & returns number of characters added"""
    #  "a" >> append mode
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
    