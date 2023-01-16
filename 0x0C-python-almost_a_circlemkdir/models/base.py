#!/usr/bin/python3
"""module for Base class"""

class Base:
    """Class base
    Args:
        id: an interger.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor."""
        if id is None:
            Base.__nb_objects += 1
            self.if = Base.__nb_objects
        else:
            self.id = id
