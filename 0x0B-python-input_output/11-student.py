#!/usr/bin/python3
"""
===============================
module with the class Student
===============================
"""


class Student:
    """student class with method to_json and
    reload_from_json"""

    def __init__(self, first_name, last_name, age):
        """initializing all attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that retrieves a dictionary representation 
        of a Student instance"""

        if attrs is None:
            return self.__dict__
        new_dic = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dic[key] = value
        return new_dic

    def reload_from_json(self, json):
        """method hat replaces all attributes of the 
        Student instance"""

        for key, value in json.items():
            self.__dict__[key] = value
