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
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    try:
        result = int(a) + int(b)
    except OverflowError:
        raise OverflowError("integer value too large")
    return result
