#!/usr/bin/env python3
""" This is the Convert CSV Data to JSON module
"""
import csv
import json


def convert_csv_to_json(filename):
    """ Convert csv file to json"""
    # open the csv file and read the data
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))

    with open('data.json', mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)
