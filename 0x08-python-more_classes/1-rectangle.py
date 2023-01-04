#!/usr/bin/python3
"""
A Rectangle class.
"""


class Rectangle:
    """
    This class creates private instances attributes
    Args:
        width : Is an int of the horizontal of the rectangle.
        height: Is an int of the vertical sides of the rectangle.
    """
        def __init__(self, width=0, height=0):
            # Initialize a new rectangle
            self.width = width
            self.height = height

        @property
        def width(self):
            # sets the horizontal sides of the rectangle
            return self.__width

        @width.setter
        def width(self, value):
            """
            Raises:
                TypeError: if value is not an int.
                ValueError: If value is less than 0.
            """
            if type(value) is not int:
                raise TypeError('width must be an integer')
            elif value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

        @property
        def height(self):
            # Sets the vertical sides of a rectangle
            return self.__height

        @height.setter
        def height(self, value):
            """
            Raises:
                TypeError: if value is not an int.
                ValueError: if the value is less than 0.
            """
            if type(value) is not int:
                raise TypeError('height must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
