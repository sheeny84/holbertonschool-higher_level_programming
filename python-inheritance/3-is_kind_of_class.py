#!/usr/bin/python3
"""
This is the "is_kind_of_class" module

"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class ;
    otherwise, return False.
    """
    return isinstance(obj, a_class)
