"""Unittest for the `Base` class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Handling of `Base` class test cases"""
    def test_with_no_arguments(self):
        """Tests with no argument passed to object"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_argument(self):
        """Test with one object created but with argument"""
        Base._Base__nb_objects = 0
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_with_and_without_argument(self):
        """Test with multiple objects with object with argument
        and one without argument last"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b5.id, 3)

    def test_multiple_obj_with_arg_last(self):
        """Test with multiple objects with the one with
        the argument last"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

