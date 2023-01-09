#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
===========================
module with class Rectangle
===========================
"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Method that initializes attributes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method that calculates area"""

        return self.__width * self.__height

    def __str__(self):
        """methos to return a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
