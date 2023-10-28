#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = "none"
        return res
    finally:
        print("Inside result: {}".format(a, b, res))
    return res
