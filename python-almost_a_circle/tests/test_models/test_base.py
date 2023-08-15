#!/usr/bin/python3
"""
Unittest for Base class
"""
import unittest
from models.base import Base


class testclass(unittest.TestCase):
    """
    This class contains unittests for Base class
    """
    def test_id(self):
        """
        method that holds the tests related to id
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base(5)
        self.assertEqual(b1.id, 5)
