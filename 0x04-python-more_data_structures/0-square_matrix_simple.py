#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    mtx = matrix.copy()
    len_g = len(mtx)
    j = 0

    if mtx:
        for i in mtx:
            sm = list(map(lambda x: x**2, i))
            mtx[j] = sm
            j += 1
    return mtx
