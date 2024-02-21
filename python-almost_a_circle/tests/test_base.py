import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_assignment(self):
        """Test automatic id assignment."""
        Base._Base__nb_objects = 0  # Resetting the count consistent testing
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test conversion of dictionary to JSON string."""
        dictionary = {'id': 10, 'width': 7, 'height': 2, 'x': 0, 'y': 0}
        json_str = Base.to_json_string([dictionary])
        self.assertIsInstance(json_str, str)

    def test_from_json_string(self):
        """Test conversion of JSON string to dictionary."""
        json_str = '[{"id": 10, "width": 7, "height": 2, "x": 0, "y": 0}]'
        dictionaries = Base.from_json_string(json_str)
        self.assertIsInstance(dictionaries, list)


if __name__ == "__main__":
    unittest.main()
