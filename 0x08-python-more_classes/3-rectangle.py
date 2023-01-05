#!/usr/bin/python3
"""
A class that defines a rectangle
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Args:
            width: horizontal sides of the rectangle.
            height: vertical sides of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        #sets the horizontal side of the rectangle.
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raises:
            TypeError: if value is not an int.
            ValuesError: if valuse is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        #sets the vertical side of the rectangle
        return self.__height

    @height.setter
    def height(self, value):
        """
        Raises:
            TypeError: if value is not an int.
            ValuesError: if valuse is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []

        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
