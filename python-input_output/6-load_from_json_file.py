#!/usr/bin/python3
"""
This module contains a function that creates an object from a JSON file. It
demonstrates how to use the json module in Python to deserialize a JSON
formatted file into a Python data structure.
"""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The path to the JSON file to deserialize.

    Returns:
        The Python data structure represented by the JSON file content.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
    # This block is for demonstration and testing.
    # It will not be executed when importing this script as a module.
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file

    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
