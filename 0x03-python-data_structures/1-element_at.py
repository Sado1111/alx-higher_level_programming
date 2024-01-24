#!/usr/bin/python3
def element_at(my_list, idx):
    lens = len(my_list)
    if (idx > -(lens + 1) | idx < lens):
        return (my_list[idx])
