#!/usr/bin/python3
"""
program that imports the function def add(a, b):
    from the file add and prints the result of the addition 1 + 2 = 3
"""

from 0-import_add import add

if __name__ == "__main__":

    a = 1
    b = 2
    sums = int(add(1, 2))
    print("{} + {} = {:d}".format(a, b, sums))
