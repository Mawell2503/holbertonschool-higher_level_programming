#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    #  copy everything from my_list to new_list
    new_list = my_list[:]
    #  check idx is between 0 and the last valid index
    if 0 <= idx < len(new_list):
        #  replace the element at position idx
        new_list[idx] = element
    return new_list
