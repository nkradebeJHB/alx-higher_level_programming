#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
================================
module with class Square
================================
"""


class Square(Rectangle):
    """class square that inherits from Rectangle """
    def __init__(self, size):
        """method that initializes attributes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of a square"""

        return self.__size ** 2
