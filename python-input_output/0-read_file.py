#!/usr/bin/python3
"""
This is the read_file module
"""


def read_file(filename=""):
    """
    Read a text file and print it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
