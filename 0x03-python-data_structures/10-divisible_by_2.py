#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    t_list = my_list[:]
    for i, j in enumerate(my_list):
        if j % 2 == 0:
            t_list[i] = True
        else:
            t_list[i] = False
    return (t_list)
