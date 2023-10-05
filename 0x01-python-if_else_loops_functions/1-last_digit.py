#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
clo_num = number
sign = 1
if number < 0:
    number = -number
    sign = -1
    if (number % 10) == 0:
        print(f"Last digit of {clo_num} is 0 and is 0")
    else:
        print(f"Last digit of {clo_num} is {sign *(number % 10)}\
                and is less than 6 and not 0")
else:
    if (number % 10) == 0:
        print(f"Last digit of {clo_num} is 0 and is 0")
    elif (number % 10) < 6:
        print(f"Last digit of {clo_num} is {number % 10}\
                and is less than 6 and not 0")
    elif (number % 10) > 5:
        print(f"Last digit of {clo_num} is {sign * (number % 10)}\
                and is greater than 5")
