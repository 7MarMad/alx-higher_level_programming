#!/usr/bin/python3
# if __name__ == "__main__":
def magic_calculation(a, b):
    import magic_calculation_102
    add = magic_calclation_102.add
    sub = magic_calclation_102.sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return (sub(a, b))
