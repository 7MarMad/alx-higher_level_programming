#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        len1 = len(sentence)
        char = sentence[0]
    else:
        len1 = 0
        char = None
    tup = (len1, char)
    return tup
