#!/usr/bin/python3
"""
This is the "print_square" module.

The print_square module supplies one function,
print_square().  For example,

>>> print_square(4)
    ####
    ####
    ####
    ####
"""


def print_square(size):
    """
    Print a square of size using #
    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, int(size)):
        print(int(size)*"#")
    