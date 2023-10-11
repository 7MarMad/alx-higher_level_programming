#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_l = []

    for i in my_list:
        if i != search:
            new_l.append(i)
        elif i == search:
            new_l.append(replace)

    return new_l
