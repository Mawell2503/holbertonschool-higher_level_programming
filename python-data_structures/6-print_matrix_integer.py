#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    #  loop through matrix
    for row in matrix:
        #  loop through each row
        for i, val in enumerate(row):
            #  print a space before eery value except the first
            if i != 0:
                print(" ", end="")
            #  print the value
            print("{:d}".format(val), end="")
        print()
