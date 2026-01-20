#!/usr/bin/python3 
def print_list_integer(my_list=[[]]):
    for row in my_list:
        for i, num in enumerate(row):
            if i != len(row) -1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end="")
        print()
