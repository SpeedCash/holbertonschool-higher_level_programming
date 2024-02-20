#!/usr/bin/python3
"""
This module contains a function that writes an object to a text file, using
a JSON representation. It demonstrates file writing and JSON serialization
in Python.
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using a JSON representation.

    Args:
        my_obj: The object to serialize and write.
        filename (str): The name of the file where to write the object.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


if __name__ == "__main__":
    # This block is for demonstration and testing.
    # It will not be executed when importing this script as a module.
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = {132, 3}
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))