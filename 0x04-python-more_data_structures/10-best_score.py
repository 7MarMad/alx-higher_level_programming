#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        lis_val = list(a_dictionary.values())
        lis_key = list(a_dictionary.keys())

        lis_val.sort(reverse=True)
        maxx = lis_val[0]

        liss_val = list(a_dictionary.values())
        ind = liss_val.index(maxx)

        key = lis_key[ind]

        return key
