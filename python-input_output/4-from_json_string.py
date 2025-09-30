#!/usr/bin/python3
"""
This is the from_json_string module
"""
import json


def from_json_string(my_str):
    """
    Return the object presented by a JSON string
    """
    return json.loads(my_str)
