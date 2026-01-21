#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    #  create set
    diff = set()
    #  loop through set_1
    for element in set_1:
        #  if element is not in set_2
        if element not in set_2:
            #  add element in set
            diff.add(element)
        #  loop through set_2
        for element in set_2:
            # if element is not in set_1
            if element not in set_1:
                #  add element in set
                diff.add(element)
    return diff
