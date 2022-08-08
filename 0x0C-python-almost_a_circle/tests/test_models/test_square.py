"""Contains unittest cases for `Square` class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests all methods and attributes of the `Square`
    class
    """
    def test_size(self):
        """Test creating `Square` with integer size"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_with_zero(self):
        """Test size with zero"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)
            self.assertEqual(e, "width must be > 0")

    def test_size_with_negative(self):
        """Test size with negative number"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(-3)
            self.assertEqual(e, "width must be > 0")

    def test_size_string(self):
        """Test size with string"""
        with self.assertRaises(TypeError) as e:
            s1 = Square("5k")
            self.assertEqual(e, "width must be an integer")

    def test_size_list(self):
        """Test size with list"""

