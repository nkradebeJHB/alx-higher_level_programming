#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []

    for i in matrix:
        squared_matrix.append(list(map(lambda i: i**2, i)))
    return (squared_matrix)
