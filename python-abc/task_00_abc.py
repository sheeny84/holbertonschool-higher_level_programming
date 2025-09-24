#!/usr/bin/env python3
"""
This is the "Animal" module.

"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Define abstract method for sound an animal makes
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Return the sound a dog makes i.e. Bark
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Return the sound a cat makes i.e. Bark
    """
    def sound(self):
        return "Meow"
