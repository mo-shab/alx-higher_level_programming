#!/usr/bin/python3
"""Define a Class Square."""

class Square:
    """ square Class that have attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """ Initialization function for the square class
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        Getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """ Calculate and return the area of the square
        """
        return self.__size ** 2

    def __validate_size(self, size):
        """
        Validates the size.
        Checking for errors.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
