#!/usr/bin/python3
"""
This is the "Square" class

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Create a new instance of Square and validate size
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    """
    Define string for Square
    """
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
