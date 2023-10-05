#!/usr/bin/python3
import sys
print("{} argument".format(len(sys.argv) - 1), end="")
if len(sys.argv) == 1:
    print("s.")
elif len(sys.argv) == 2:
    print(":")
    print("1: {}".format(sys.argv[1]))
elif len(sys.argv) > 2:
    print("s:")
    for i in range(len(sys.argv) - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
