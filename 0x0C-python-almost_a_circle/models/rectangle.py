#!/usr/bin/python3

"""Module for Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """
    A Rectangle class.
    Args:
        width: horizontal side of the rectangle.
        height: vertical side of the rectangle.
        x: horizontal point of the rectangle.
        y: vertical side of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            self.is_int_valid("width", value, False)
            self.__width = value

        @property
        def height(self):
            """height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            self.is_int_valid("height", value, False)
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.is_int_valid("x", value)
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.is_int_valid("y", value)
            self.__y = value

        def is_int_valid(self, name, value, check=True):
            """method to validate value is int"""
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
            if check and value < 0:
                raise ValueError("{} must be >= 0".format(name))
            elif not check and value <= 0:
                raise ValueError("{} must be > 0".format(name))
