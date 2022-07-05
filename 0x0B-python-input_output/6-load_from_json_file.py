#!/usr/bin/python3
"""Module for save_to_json function."""


import json


def load_from_json_file(filename):
    """This function loads json from file and convert it to pyobject'''
    with open(filename, mode='r', encoding='utf-8') as f:
        my_object = json.load(f)
    return my_object
