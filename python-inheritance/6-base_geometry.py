#!/usr/bin/python3


class BaseGeometry:
    """A class BaseGeometry with unimplemented area method."""

    def area(self):
        """Raises an Exception with a message indicating the method\
            is not implemented."""
        raise Exception("area() is not implemented")
    