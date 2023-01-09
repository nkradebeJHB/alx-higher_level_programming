#!/usr/bin/python3

"""
=========================
Module with method lookup
=========================
"""


def lookup(obj):
    """
    Function that return a list of attributes and 
    methods of an object.
    """
    return dir(obj)
