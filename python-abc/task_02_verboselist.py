#!/usr/bin/env python3
"""
This is the "VerboseList" module.

"""


class VerboseList(list):
    """
    The VerboseList class inherits from list and adds notification messages
    when an item is added or removed from the list
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            print("Popped [{}] from the list.".format(self[-1]))
            super().pop()
        else:
            print("Popped [{}] from the list.".format(self[index]))
            super().pop(index)
