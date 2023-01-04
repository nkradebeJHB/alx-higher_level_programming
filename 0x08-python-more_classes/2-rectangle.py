#!/usr/bin/python3
"""
A Rectangle class
"""


class Rectangle:
    """
    Rectangle class 
    Args:
        width: horizontal sides of the rectangle.
        height: vertical sides of the rectangle.
    """
    def __init__(self, width=0, height=0):
        # initializes the width and height of a new rectangle
        self.width = width
        self.height = height

    @property
    def width(self):
        #Sets the horizontal side of the rectangle.
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raises:
            TypeError: if value is not an int.
            ValuesError: if valuse is less than 0.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        # Sets the vertical sides of the rectangle
        return self.__width

    @height.setter
    def height(self, value):
        """
        Raises:
            TypeError: if value is not an int.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns:
            0 if the is a 0 as an attribute,
            or the perimeter of the rectangle.
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
