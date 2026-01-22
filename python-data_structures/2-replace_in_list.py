#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    #  if idx is less than 0
    if idx < 0:
        #  return original list
        return my_list
    #  if idx is greater than len of my_list
    if idx >= len(my_list):
        #  return original list
        return my_list
    my_list[idx] = element
    return my_list
