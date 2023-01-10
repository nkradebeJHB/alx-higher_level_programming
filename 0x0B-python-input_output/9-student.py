#!/usr/bin/python3
"""
=========================
module with class student 
=========================
"""


class Student:
    """Student class with methods to_json"""

    def __init__(self, first_name, last_name, age):
        """initailizing all attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
