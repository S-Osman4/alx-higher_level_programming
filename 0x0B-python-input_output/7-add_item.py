#!/usr/bin/python3
"""Module to append elements in a json file."""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""dump: create an object using a json and save it to a .txt file"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""load: read a file and convert json data to object."""

try:
    container = load_from_json_file('add_item.json')
except:
    container = []

for i in range(1, len(sys.argv)):
    container.append(sys.argv[i])
save_to_json_file(container, 'add_item.json')
