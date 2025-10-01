#!/usr/bin/env python3
""" This is the Serialize and Deserialize with XML module
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serialize dictionary into XML and save to filename"""
    elem = ET.Element("data")
    for key, val in dictionary.items():
        child = ET.SubElement(elem, key)
        child.text = str(val)
    tree = ET.ElementTree(elem)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Read XML data from file and return deserialized
    python dictionary
    """
    tree = ET.parse(filename)
    dict = {}
    root = tree.getroot()
    for child in root:
        dict[child.tag] = child.text
    return dict
