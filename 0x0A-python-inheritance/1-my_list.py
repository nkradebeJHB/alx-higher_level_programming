#!/usr/bin/python3
"""
========================
Module with class MyList
========================
"""


class MyList(list):
    """
    Class with method print_sorted that prints the list,
    but sorted (ascending sort)
    """

    def print_sorted(self):
        """method that prints a sorted list"""

        print(sorted(list(self)))
