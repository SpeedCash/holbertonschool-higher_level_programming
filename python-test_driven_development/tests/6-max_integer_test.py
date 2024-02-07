#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
from 6-max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_max_end(self):
        """Test with the max integer at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        """Test with the max integer at the beginning of the list."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_middle(self):
        """Test with the max integer in the middle of the list."""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_element(self):
        """Test with a single element in the list."""
        self.assertEqual(max_integer([4]), 4)

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_none(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_not_int(self):
        """Test with non-integers in the list."""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3, 4])


if __name__ == "__main__":
    unittest.main()
