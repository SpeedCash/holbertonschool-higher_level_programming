import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_area(self):
        """Test area calculation."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_update(self):
        """Test the update method."""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)


if __name__ == "__main__":
    unittest.main()
