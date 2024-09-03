#!/usr/bin/python3

"""
Function that prints and returns the last digit of a number.
You are not allowed to import any module
You don’t need to understand __import__
"""


def print_last_digit(number):
    last_digit = abs(number) % 10
    print('{}'.format(last_digit), end='')
    return (last_digit)
