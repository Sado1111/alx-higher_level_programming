#!/usr/bin/python3
def element_at(my_list, idx):
    lens = len(my_list)
    if (idx > -1 and idx < lens):
        return (my_list[idx])
    return None
