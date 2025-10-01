#!/usr/bin/env python3
""" This is the Basic Serialization module
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """ Serialize and save data to specified file
    """
    with open(filename, mode='wb') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """ Deserialize data from specified file
    """
    with open(filename, "rb") as f:
        return pickle.load(f)
