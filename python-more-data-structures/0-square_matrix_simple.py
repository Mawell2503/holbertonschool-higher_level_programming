#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #  create a list
    new_list = []
    #  loop through each row of the matrix
    for row in matrix:
        #  for each row create a number list
        num_list = []
        #  loop through each number of the row
        for num in row:
            #  add the squared value to the number list
            num_list.append(num * num)
        #  add the number list to the first list created
        new_list.append(num_list)
    #  return the new list
    return new_list

