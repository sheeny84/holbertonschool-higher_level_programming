#!/usr/bin/python3
""" This is the Student Class module
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        """ Initiliase class with first name, last name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return dictionary representation of a Student instance
        """
        return self.__dict__
