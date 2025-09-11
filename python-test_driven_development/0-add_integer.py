#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        a = int(a)
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")
    return a + b
