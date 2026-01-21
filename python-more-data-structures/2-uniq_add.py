#!/usr/bin/python3
def uniq_add(my_list=[]):
    #  create a set 
    unique_values = set()
    for value in my_list:
        unique_values.add(value)
        total = 0
    for value in unique_values:
        total = total + value
    return total
