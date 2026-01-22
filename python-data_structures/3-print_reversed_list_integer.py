#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    #   loop through range
    for i in range(len(my_list)-1, -1, -1):
        #  print whats in range
        print("{:d}".format(my_list[i]))
