#!/usr/bin/env python3
""" This is the CustomObject Class module
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """ Initialise new CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ Display CustomObject attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """ Serialize and save data to specified filename
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(csl, filename):
        """ Deserialize data from specified file
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
