#!/usr/bin/python3

"""
========================================================
Module for Rectangle class that inherits form class Base
========================================================
"""

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
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            self.__height = height

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, x):
            self.__x = x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, y):
            self.__y = y
