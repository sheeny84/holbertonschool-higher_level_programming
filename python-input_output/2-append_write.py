#!/usr/bin/python3
"""
This is the append_write module
"""


def append_write(filename="", text=""):
    """
    Append a string to a text file
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
