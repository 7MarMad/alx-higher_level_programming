#!/usr/bin/python3

def remove_char_at(str, n):
    sttr = str
    if n < 0:
        return sttr
    sttr = sttr[:n] + sttr[n + 1:]
    return sttr
