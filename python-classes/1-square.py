#!/usr/bin/python3
"""
This is the "Square" class module.

"""


class Square:
    """
    This is a Square class
    """
    def __init__(self, size):
        """
        Initialise a new instance of Square 
        with size and an empty dictionary

        Args:
            size (int): Size of the square
        """
        self.__dict__ = {}
        self.__size = size
