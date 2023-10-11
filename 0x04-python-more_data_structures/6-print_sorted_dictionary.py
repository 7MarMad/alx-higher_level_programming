#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dic = {}
    llist = sorted(a_dictionary)

    for i in llist:
        dic[i] = a_dictionary[i]
    for j, m in dic.items():
        print("{}: {}".format(j, m))
