#!/usr/bin/python3
"""
Function that prints a string in uppercase followed by a new line.

You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
"""


def uppercase(str):
    for i in str:
        if i.isalpha():
            if 97 <= ord(i) <= 122:
                i = chr(ord(i) - 32)
        print('{}'.format(i), end='')
    print(''.format())
