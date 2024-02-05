#!/usr/bin/python3

class Square:
    """Class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with size (no type/value verification)"""
    
    def __init__(self, size):
        """Initialize the Square instance with a size."""
        self.__size = size
