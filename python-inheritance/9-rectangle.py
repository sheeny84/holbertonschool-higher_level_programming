#!/usr/bin/python3
"""
This is the "Rectangle" class

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Create a new instance of Rectangle and validate width and height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """
    Return the area of the Rectangle
    """
    def area(self):
        return self.__width * self.__height

    """
    Define string for Rectangle
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    """
    Define print for Rectangle
    """
    def __print__(self):
        print(self.__print__)
