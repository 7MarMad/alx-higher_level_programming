#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    m = 0
    try:
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
                m += 1
            except (ValueError, TypeError):
                pass
        print("")
    except IndexError:
        print("")

    return m
