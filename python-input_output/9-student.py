#!/usr/bin/python3
"""
This module defines a Student class which initializes with first_name,
last_name, and age attributes and includes a method to retrieve a
dictionary representation of the instance.
"""


class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes the student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
