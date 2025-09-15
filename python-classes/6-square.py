#!/usr/bin/python3
"""
This is the "Square" class module.

"""


class Square:
    """
    This is a Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise a new instance of Square
        with default size of 0 and an empty dictionary

        Args:
            size (int): Size of the square
            position (tuple): coordinates of the
            starting position of the square
        """
        self.__dict__ = {}
        self.__size = size
        self.__position = position

    def area(self):
        """
        Return the current square area
        """
        return self.__size**2

    @property
    def size(self):
        """
        Return the current square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the current square size

        Args:
            size (int): Size of the square
        """
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Return the current square position
        """
        return self.__position

    @size.setter
    def position(self, value):
        """
        Set the current square position

        Args:
            value (tuple): position coordinates
        """
        if not isinstance(value[0], int) or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print the current square with the character #
        """
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            print(self.__position[0]*" ", end="")
            print("#"*self.__size)
        if self.__size == 0:
            print()
