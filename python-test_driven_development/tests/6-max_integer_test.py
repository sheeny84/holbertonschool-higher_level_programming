#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_at_the_end(self):
        self.assertTrue(max_integer([1, 4, 6]), 6)

    def test_max_at_the_beginning(self):
        self.assertTrue(max_integer([6, 4, 1]), 6)
    
    def test_max_in_the_middle(self):
        self.assertTrue(max_integer([1, 6, 4]), 6)
    
    def test_one_negative(self):
        self.assertTrue(max_integer([1, 4, -6, 2, 3]), 4)

    def test_all_negative(self):
        self.assertTrue(max_integer([-1, -4, -6]), -1)

    def test_one_element(self):
        self.assertTrue(max_integer([2]), 2)

    def test_empty_list(self):
        self.assertTrue(max_integer(), None)

    def test_not_integer(self):
        self.assertRaises(TypeError, max_integer("string"))


if __name__ == '__main__':
    unittest.main()
