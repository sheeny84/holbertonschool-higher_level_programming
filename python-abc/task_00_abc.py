#!/usr/bin/env python3
"""
This is the "Animal" module.

"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This is a generic Animal abstract class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    This is the Dog class that inherits from the Animal class
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    This is the Cat class that inherits from the Animal class
    """
    def sound(self):
        return "Meow"
