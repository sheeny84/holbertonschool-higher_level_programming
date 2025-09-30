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

    def to_json(self, attrs=None):
        """
        Return dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved
        Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for element in attrs:
                try:
                    my_dict[element] = getattr(self, element)
                except AttributeError as e:
                    pass
        return my_dict
