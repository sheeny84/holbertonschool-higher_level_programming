#!/usr/bin/python3
"""
This is the write_file module
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
