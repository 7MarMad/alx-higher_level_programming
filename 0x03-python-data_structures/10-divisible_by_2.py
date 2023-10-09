#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        len1 = len(my_list)
        n_list = [False] * len1

        for i in range(len1):
            if (my_list[i] % 2 == 0):
                n_list[i] = True
        return n_list
