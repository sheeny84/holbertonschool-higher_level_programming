#!/usr/bin/python3
"""
This is the "add_integer" module.

The add_integer module supplies one function, add_integer().  For example,

>>> add_integer(1, 2)
3
"""
def add_integer(a, b=98):
    """
    Return the addition of two integers
    """
    try:
        a = int(a)
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")
    return a + b
