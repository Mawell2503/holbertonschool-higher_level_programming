#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    indxA1 = tuple_a[0]
    indxA2 = tuple_a[1]
    indxB1 = tuple_b[0]
    indxB2 = tuple_b[1]
    return (indxA1 + indxB1, indxA2 + indxB2)
