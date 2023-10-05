#!/usr/bin/python3
def pow(a, b):
    c = a
    if b == 0:
        return 1
    for i in range(2, b + 1):
        c = c * a
    if b > 0:
        return c
    else:
        return (1 / c)
