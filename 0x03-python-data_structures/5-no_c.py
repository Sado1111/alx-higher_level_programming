#!/usr/bin/python3

"""
Write a function that removes all characters c and C from a string.
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()
"""


def no_c(my_string):
    if my_stringi:
        new_str = ''
        for ch in my_string:
            if ch == 'c' or ch == 'C':
                ch = ''
            new_str += ch
        return new_str
