#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstabce(my_list, list):
        my_list.reverse()
        for i in my_list:
            print('{:d}'.format(my_list[i]))
