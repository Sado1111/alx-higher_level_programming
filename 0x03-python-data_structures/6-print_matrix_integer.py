#!/usr/bin/python3
"""
function that prints a matrix of integers.

    Prototype: def print_matrix_integer(matrix=[[]]):
    Format: see example
    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers
"""


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for num in row:
                print('{:d}'.format(num), end=' ' if num != row[-1] else '')
            print()
    else:
        print()
