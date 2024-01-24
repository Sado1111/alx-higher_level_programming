#!/usr/bin/python3
def element_at(my_list, idx):
    lens = len(my_list)
    if (idx < -(lens) | idx > (lens - 1)):
        return (None)
    else:
        return (my_list[idx])
