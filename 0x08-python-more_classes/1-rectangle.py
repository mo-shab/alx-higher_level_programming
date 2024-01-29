#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, height = 0, width = 0):
        self._width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter method for height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self._height = value
