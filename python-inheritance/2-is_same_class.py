#!/usr/bin/python3
"""
This is the "is_same_class" module.

"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class
    otherwise, return False.
    """
    return type(obj) is a_class
