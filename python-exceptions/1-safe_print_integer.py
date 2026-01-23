#!/usr/bin/python3
def safe_print_integer(value):
    #  try this code: if successful return true else false
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
