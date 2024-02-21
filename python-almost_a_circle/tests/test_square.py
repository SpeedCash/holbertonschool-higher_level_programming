import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_size(self):
        """Test size assignment and retrieval."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_area(self):
        """Test area calculation for square."""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_update(self):
        """Test the update method for square."""
        s1 = Square(1, 1, 1, 1)
        s1.update(size=7, id=89, y=1, x=2)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)


if __name__ == "__main__":
    unittest.main()
