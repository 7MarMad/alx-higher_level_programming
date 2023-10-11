#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = []
    for key, val in a_dictionary.items():
        if val == value:
            keys.append(key)

    for i in keys:
        del a_dictionary[i]

    return a_dictionary
