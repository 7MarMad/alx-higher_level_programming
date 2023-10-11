#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dic = {}
    llist = a_dictionary.keys()

    for i in llist:
        dic[i] = (a_dictionary.get(i)) * 2

    return dic
