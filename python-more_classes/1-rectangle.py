#!/usr/bin/python3
"""
This is the "Rectangle" class module.

"""


class Rectangle:
    """
    Initialise a new instance of the Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.__dict__ = {}
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """
        Return the width of the current rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the current rectangles width

        Args:
            width (int): width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Return the height of the current rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the current rectangles height

        Args:
            height (int): height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
