#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertTrue(max_integer([1, 4, 3]), 4)

    def test_not_integer(self):
        self.assertRaises(TypeError, max_integer("string"))


if __name__ == '__main__':
    unittest.main()
