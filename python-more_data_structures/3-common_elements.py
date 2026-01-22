#!/usr/bin/python3
def common_elements(set_1, set_2):
    #  create set
    common = set()
    #  loop through set_1
    for element in set_1:
        #  while looping through set_1 loop through set_2 and check for element
        if element in set_2:
            #  add element to set
            common.add(element)
            #  return the set
    return common
