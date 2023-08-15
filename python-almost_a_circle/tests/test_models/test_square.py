#!/usr/bin/python3
"""
Unittest for Square class
"""
import unittest
from models.square import Square


class testclass(unittest.TestCase):
    """
    This class contains unittests for Square class
    """
    def test_instantiation(self):
        """
        method that holds the tests related to __init__ method
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s2 = Square(5, 5, 5, None)
        self.assertNotEqual(s2.id, None)

    def test_private_attributes(self):
        """ checks if attributes are private """
        s1 = Square(5)
        with self.assertRaises(AttributeError):
            print(s1.__width)
        with self.assertRaises(AttributeError):
            print(s1.__height)
        with self.assertRaises(AttributeError):
            print(s1.__x)
        with self.assertRaises(AttributeError):
            print(s1.__y)

    def test_wrong_arguments_number(self):
        """ checks number of arguments """
        with self.assertRaises(TypeError):
            s3 = Square()
        with self.assertRaises(TypeError):
            s3 = Square(5, 5, 5, 5, 5, 5, 5, 5, 5)

    def test_validation(self):
        """
        method to test validation of width, height, x and y
        """
        with self.assertRaises(TypeError):
            s3 = Square("h", "j")
        with self.assertRaises(TypeError):
            s3 = Square(5, "j")
        with self.assertRaises(TypeError):
            s3 = Square(1, 2, "a")
        with self.assertRaises(TypeError):
            s3 = Square(1, 3, "j", 5)
        with self.assertRaises(ValueError):
            s3 = Square(0, 5)
        with self.assertRaises(ValueError):
            s3 = Square(-1, 5)
        with self.assertRaises(ValueError):
            s3 = Square(5, -2)
        with self.assertRaises(ValueError):
            s3 = Square(5, -5)
        with self.assertRaises(ValueError):
            r3 = Square(5, 5, -1, 7)

    def test_area(self):
        """ test area method """
        s3 = Square(5)
        self.assertEqual(s3.area(), 25)

    def test_str(self):
        """ test str method """
        s3 = Square(4, 2, 1, 12)
        s4 = Square(4)
        st = str(s3)
        st2 = str(s4)
        self.assertEqual(st, "[Square] (12) 2/1 - 4")
        self.assertEqual(st2, "[Square] (21) 0/0 - 4")

    def test_update(self):
        """ test update method """
        s3 = Square(5, 5, 5, 5)
        s3.update(1)
        st = str(s3)
        self.assertEqual(st, "[Square] (1) 5/5 - 5")
        s3.update(1, 1, 1, 1, 1)
        st2 = str(s3)
        self.assertEqual(st2, "[Square] (1) 1/1 - 1")

    def test_updatek(self):
        """ test update method (*args and **kwargs) """
        s3 = Square(5, 5, 5, 5)
        s3.update(1, size=1)
        st = str(s3)
        self.assertEqual(st, "[Square] (1) 5/5 - 5")
        s3.update(size=1, x=1, y=1, id=1)
        st = str(s3)
        self.assertEqual(st, "[Square] (1) 1/1 - 1")
