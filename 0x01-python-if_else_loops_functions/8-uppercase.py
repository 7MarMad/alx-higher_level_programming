#!/usr/bin/python3
def uppercasee(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            c = chr(ord(c - 32))
        print(c, end="")
    print("")