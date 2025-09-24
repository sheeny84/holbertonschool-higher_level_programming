#!/usr/bin/env python3
"""
This is the "CountedIterator" module.

"""


class CountedIterator():
    """
    The CountedIterator class extends the built-in
    iterator object from the iter function
    """
    def __init__(self, list):
        self.my_iterator = iter(list)
        self.counter = 0

    def __next__(self):
        self.counter += 1
        return self.my_iterator.__next__()

    def get_count(self):
        return self.counter
