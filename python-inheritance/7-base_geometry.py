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
    
    """
    Validate that value is an integer greater than 0
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError ("{} must be greater than 0".format(name))
