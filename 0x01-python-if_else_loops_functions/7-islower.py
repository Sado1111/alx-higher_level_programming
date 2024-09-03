#!/usr/bin/python3
"""
Function that checks for lowercase character.
Prototype: def islower(c):
Returns True if c is lowercase
Returns False otherwise
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
"""


def islower(c):
    """ Function that returns true if c is lowercase """
    return (97 <= ord(c) <= 122)
