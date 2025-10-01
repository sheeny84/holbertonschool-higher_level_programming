#!/usr/bin/env python3
""" This is the Basic Serialization module
"""
import json


def serialize_and_save_to_file(data, filename):
    """ Serialize and save data to specified file
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """ Deserialize data from specified file
    """
    with open(filename, "r") as f:
        return json.load(f)
