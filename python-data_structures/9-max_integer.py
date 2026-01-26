#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    biggest_int = my_list[0]
    for number in  my_list:
         if number > biggest_int:
             biggest_int = number
    return biggest_int
