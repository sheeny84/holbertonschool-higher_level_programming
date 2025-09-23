#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This is the "Rectangle" class

"""


class Rectangle(BaseGeometry):
    """
    Create a new instance of Rectangle and validate width and height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
