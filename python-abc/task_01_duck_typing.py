#!/usr/bin/env python3
"""
This is the "Shape" module.

"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    The Shape class is a generic abstract class with two abstract
    methods: area; and perimeter.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    This is the Circle class that inherits from Shape and
    requires a radius on initialisation
    """
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    This is the Rectangle class that inherits from Shape and
    requires width and height on initialisation
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * self.__width + 2 * self.__height


def shape_info(self):
    print("Area: {}".format(self.area()))
    print("Perimeter: {}".format(self.perimeter()))
