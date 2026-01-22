#!/usr/bin/python3
def no_c(my_string):
    #  create an empty string
    result = ""
    # loop through my_string
    for char in my_string:
        #  check that character is not 'c' or 'C'
        if char != 'c' and char != 'C':
            #  add character to the resultes string
            result += char
    return result
