#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_mx = []
    for line in matrix:
        square_mx.append([c**2 for c in line])
    return square_mx
