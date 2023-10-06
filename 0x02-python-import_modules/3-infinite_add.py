#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv)
    sum_o = 0
    for i in range(1, leng):
        sum_o = sum_o + int(sys.argv[i])
    print(sum_o)
