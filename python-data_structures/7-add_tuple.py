#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #  if at least 1 element, take the first element; otherwise, use 0
    indxA1 = tuple_a[0] if len(tuple_a) > 0 else 0
    #  if second element exist take it; otherwise use 0.
    indxA2 = tuple_a[1] if len(tuple_a) > 1 else 0
    indxB1 = tuple_b[0] if len(tuple_b) > 0 else 0
    indxB2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (indxA1 + indxB1, indxA2 + indxB2)
