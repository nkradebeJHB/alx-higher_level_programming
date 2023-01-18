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
            return self._width

        @width.setter
        def width(self, width):
            if type(width) is not int:
                raise TypeError("width must be an integer")
            elif width <= 0:
                raise ValueError("width must be > 0")
            else:
                self._width = width

        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, height):
            if type(height) is not int:
                raise TypeError("height must be an integer")
            elif height <= 0:
                raise ValueError("height must be > 0")
            else:
                self._height = height

        @property
        def x(self):
            return self._x

        @x.setter
        def x(self, x):
            if type(x) is not int:
                raise TypeError("x must be an integer")
            elif x < 0:
                raise ValueError("x must be >= 0")
            else:
                self._x = x

        @property
        def y(self):
            return self._y

        @y.setter
        def y(self, y):
            if type(y) is not int:
                raise TypeError("y must be an integer")
            elif y < 0:
                raise ValueError("y must be >= 0")
            else:
                self._y = y

        def area(self):
            """method to determine the area of a rectangle"""

            return self.width * self.height
