#!/usr/bin/python3
"""
function that replaces an element in a list at
a specific position without modifying the original list
"""


def new_in_list(my_list, idx, element):
    if my_list and idx > -1 and idx < len(my_list):
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    return (my_list)
