#!/usr/bin/python3
def uniq_add(my_list=[]):
    #  create a set
    unique_values = set()
    #  loop through the list
    for value in my_list:
        #  add the values to the set(.add() only add an item once) 
        unique_values.add(value)
        #  create variable for the addition
    total = 0
    # loop through the new set
    for value in unique_values:
        #add every value 
        total = total + value
    #  return the addition
    return total
