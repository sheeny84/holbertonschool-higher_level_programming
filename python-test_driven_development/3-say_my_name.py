#!/usr/bin/python3
"""
This is the "say_my_name" module.

The say_my_name module supplies one function,
say_my_name().  For example,

>>> say_my_name("Sheeny", "Soulsby")
    My name is Sheeny Soulsby
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first name> <last name>"
    """
    if not first_name:
        raise TypeError("say_my_name() missing 1 required "
                "positional argument: 'first_name")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
