#!/usr/bin/python3
"""
A script that adds all arguments to a Python list, and then save them\
    to a file.
The list is saved as a JSON representation in a file named add_item.json.
"""
import sys

# Importing the necessary functions from previous tasks
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# The filename where the list should be saved
filename = "add_item.json"

try:
    # Try to load the existing list from file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list
    items = []

# Add all arguments passed to the script to the list
# (excluding the first argument, which is the script name itself)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
