#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    strg = a_dictionary.copy()

    for i in strg.keys():
        strg[i] *= 2
    return (strg)
