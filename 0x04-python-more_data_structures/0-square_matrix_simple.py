#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    mtx = matrix.copy()
    len_g = len(mtx)

    for i in range(len_g):
        len_l = len(mtx[i])
        for j in range(len_l):
            mtx[i][j] = mtx[i][j]**2
    return mtx
