#!/usr/bin/python3
"""
This is the "MyList" class.

"""


class MyList(list):
    """
    Print the list sorted in ascending order
    """
    def print_sorted(self):
        print(sorted(self))
