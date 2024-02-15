#!/usr/bin/python3
"""
This module contains a function that returns the JSON representation of an object
(string). It demonstrates the use of the json module in Python to serialize objects.
"""

import json

def to_json_string(my_obj):
    """Return the JSON representation of an object (string).
    
    Args:
        my_obj: The object to serialize.
        
    Returns:
        str: The JSON representation of my_obj.
    """
    return json.dumps(my_obj)
