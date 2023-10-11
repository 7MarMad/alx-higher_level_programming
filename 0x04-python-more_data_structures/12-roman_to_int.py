#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        list_o = {
                'M': 1000, 'D': 500, 'C': 100,
                'L': 50, 'X': 10, 'V': 5, 'I': 1}
        prob = ['C', 'X', 'I']

        summ = 0
        len1 = len(roman_string)
        for i in range(len1):
            val = 0
            if (i != len1 - 1) and roman_string[i] in prob:
                if roman_string[i] == 'C':
                    if roman_string[i + 1] in ('D', 'M'):
                        val = 1
                        summ -= 100
                elif roman_string[i] == 'X':
                    if roman_string[i + 1] in ('L', 'C'):
                        val = 1
                        summ -= 10
                elif roman_string[i] == 'I':
                    if roman_string[i + 1] in ('X', 'V'):
                        val = 1
                        summ -= 1
            if val == 0:
                summ += list_o[roman_string[i]]
        return summ

    else:
        return 0
