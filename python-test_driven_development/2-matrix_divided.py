#!/usr/bin/python3
def matrix_divided(matrix, div):
    #  Exceptions
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_len = len(matrix[0])
        for row_len in matrix:
            if len(row) != row_len:
                raise TypeError ("Each row of the matrix must have the same size")
        for value in row:
            if type(value) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")    
    for div in row:
        if type(div) not in (int, float):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        
    #divisions
    result =[]
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(round(value / div, 2))
        result.append(new_row)
    return result
