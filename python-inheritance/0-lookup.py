#!/usr/bin/python3
def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj (Any): The object to inspect.

    Returns:
        list: A list of strings, each string being an attribute\
            or method name of `obj`.
    """
    return dir(obj)
