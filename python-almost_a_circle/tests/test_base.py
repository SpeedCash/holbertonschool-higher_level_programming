#!/usr/bin/python3
"""
Unittest for the Base class in the base.py module.
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Define unittests for the Base class."""

    def setUp(self):
        """Reset the private class attribute _Base__nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_assignment_auto(self):
        """Test automatic id assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)

    def test_id_assignment_manual(self):
        """Test manual (specific) id assignment."""
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_id_negative(self):
        """Test negative id assignment."""
        b1 = Base(-10)
        self.assertEqual(b1.id, -10)

    def test_id_zero(self):
        """Test id assignment with zero."""
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_to_json_string(self):
        """Test conversion of dictionary to JSON string."""
        dictionary = {'id': 10, 'width': 7, 'height': 2, 'x': 0, 'y': 0}
        json_str = Base.to_json_string([dictionary])
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, '[{"id": 10, "width": 7, "height": 2, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        """Test conversion of JSON string to dictionary."""
        json_str = '[{"id": 10, "width": 7, "height": 2, "x": 0, "y": 0}]'
        result = Base.from_json_string(json_str)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [{"id": 10, "width": 7, "height": 2, "x": 0, "y": 0}])

    def test_json_string_empty(self):
        """Test passing an empty list to to_json_string method."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_json_string_None(self):
        """Test passing None to to_json_string method."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_from_json_string_empty(self):
        """Test passing an empty string to from_json_string method."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_None(self):
        """Test passing None to from_json_string method."""
        self.assertEqual(Base.from_json_string(None), [])

if __name__ == "__main__":
    unittest.main()
