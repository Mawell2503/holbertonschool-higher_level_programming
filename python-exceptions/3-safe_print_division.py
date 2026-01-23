#!/usr/bin/python3
def safe_print_division(a, b):
    #  confirming the existence of result
    result = None
    #  divide 2 integers
    try:
        result = a / b
    #  if error result == none
    except Exception:
        result = None
    #  print the outcome
    finally:
        print("Inside result: {}".format(result))
    return result
