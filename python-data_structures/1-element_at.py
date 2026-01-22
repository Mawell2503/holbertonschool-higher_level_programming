#!/usr/bin/python3
def element_at(my_list, idx):
    #  if 0 is greater than idx
    if idx < 0:
        # return nothng litteraly
        return None
    #  if idx is greater or equal to the length my_list
    if idx >= len(my_list):
        # return nothng litteraly
        return None
    return my_list[idx]
