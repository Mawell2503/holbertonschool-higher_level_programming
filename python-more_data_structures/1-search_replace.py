#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #  create new list
    n_list = []
    #  loop for every digit in my_list
    for digit in my_list:
        #  if digit = search
        if digit == search:
            #  replace search with replace
            n_list.append(replace)
        else:
            # keep printing the same digit
            n_list.append(digit)
    # return the new list
    return n_list
