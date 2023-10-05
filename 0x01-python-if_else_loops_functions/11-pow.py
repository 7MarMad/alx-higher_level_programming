#!/usr/bin/python3
def pow(a, b):
    c = a
    d = b
    if b == 0:
        return 1
    if b < 0:
        d = -b
    for i in range(2, d + 1):
        c = c * a
    if b > 0:
        return c
    else:
        return (1 / c)
