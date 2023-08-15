#!/usr/bin/python3
'''Tests for base class
'''
import unittest
from models.base import Base


class BaseClassTest(unittest.TestCase):
    '''Unit test for Base class inherits from unittest.TestCase
    '''

    def test_no_arg_base(self):
        '''Ensures the right value is assigned to id
        '''
        b1 = Base()
        b2 = Base()
        self.assertTrue(len(Base.__doc__))
        self.assertTrue(len(Base.__init__.__doc__))
        self.assertEqual(b1.id, b2.id - 1)

    def test_increment(self):
        '''Ensures that id is increased by 1 if no argument is supplied
        '''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)

    def test_id_args(self):
        '''checks if supplied argument is correctly handled
        '''
        b1 = Base(12)
        self.assertEqual(b1.id, Base(12).id)

    def test_id_None(self):
        '''Check class behavior with None as argument
        '''
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_id_public(self):
        '''Ensures that id is a public instance attribute
        '''
        b1 = Base(20)
        b1.id = 21
        self.assertEqual(b1.id, Base(21).id)

    def test_id_as_string(self):
        '''Tests to ensure that id is not checked for types
        '''
        b1 = Base("Shobi")
        self.assertEqual(b1.id, "Shobi")

    def test_id_as_float(self):
        '''Tests that id can be assigned to any type
        '''
        b1 = Base(2.9)
        self.assertEqual(b1.id, 2.9)

    def test_id_as_inf(self):
        '''Tests that id can be assigned to float inf
        '''
        b1 = Base(float('inf'))
        self.assertEqual(b1.id, float('inf'))

    def test_nb_objects_is_private(self):
        '''Tests that  __nb_objects is a private class attribute
        '''
        with self.assertRaises(AttributeError):
            Base.__nb_objects += 1

    def test_nb_objects(self):
        '''Tests that __nb_objects is a class attribute
        '''
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects += 1


if __name__ == "__main__":
    unittest.main()
