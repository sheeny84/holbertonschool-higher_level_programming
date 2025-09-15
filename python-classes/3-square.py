#!/usr/bin/python3
"""
This is the "Square" class module.

"""


class Square:
    """
    This is a Square class
    """
    def __init__(self, size=0):
        """
        Initialise a new instance of Square
        with default size of 0 and an empty dictionary

        Args:
            size (int): Size of the square
        """
        self.__dict__ = {}
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Return the current square area
        """
        return self.__size**2
