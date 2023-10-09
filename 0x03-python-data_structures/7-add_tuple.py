#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 < 2:
        if len1 < 1:
            tuple_aa = (0, 0)
        else:
            tuple_aa = (tuple_a[0], 0)
    else:
        tuple_aa = tuple_a
    if len2 < 2:
        if len2 < 1:
            tuple_bb = (0, 0)
        else:
            tuple_bb = (tuple_b[0], 0)
    else:
        tuple_bb = tuple_b
    tuple_c = (tuple_aa[0] + tuple_bb[0], tuple_aa[1] + tuple_bb[1])
    return (tuple_c)
