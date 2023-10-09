#!/usr/bin/python3

def no_c(my_string):
    sttr = ""
    str_list = list(my_string)
    len1 = str_list.count('c')
    len2 = str_list.count('C')

    for i in range(len1):
        str_list.remove('c')
    for j in range(len2):
        str_list.remove('C')
    return sttr.join(str_list)
