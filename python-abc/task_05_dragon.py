#!/usr/bin/env python3
"""
This is the "Dragon" module.

"""


class SwimMixin:
    """
    This is the SwinMixin class with a swim method
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    This is the FlyMixin class with a fly method
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
