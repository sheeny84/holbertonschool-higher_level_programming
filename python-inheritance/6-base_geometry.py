#!/usr/bin/python3
"""
This is the "BaseGeometry" class

"""


class BaseGeometry:
    """
    Raise an exception saying area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
