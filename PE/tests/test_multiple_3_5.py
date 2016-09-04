from django.utils import unittest
from multiple_3_5 import find_totalOf_multiple_of_3_or_5_for_range

__author__ = 'vikass'

class TestMultipleOf_3_5(unittest.TestCase):

    def test_find_totalOf_multiple_of_3_or_5_for_range_should_give_23_for_numbers_below_10(self):
        self.assertEquals(find_totalOf_multiple_of_3_or_5_for_range(10), 23)

    def test_find_totalOf_multiple_of_3_or_5_for_range_should_give_23368_for_numbers_below_10(self):
        self.assertEquals(find_totalOf_multiple_of_3_or_5_for_range(1000), 233168)

    def test_find_totalOf_multiple_of_3_or_5_for_range_should_give_0_for_numbers_below_0(self):
        self.assertEquals(find_totalOf_multiple_of_3_or_5_for_range(0), 0)

    def test_find_totalOf_multiple_of_3_or_5_for_range_should_give_0_for_numbers_below_3(self):
        self.assertEquals(find_totalOf_multiple_of_3_or_5_for_range(3), 0)

    def test_find_totalOf_multiple_of_3_or_5_for_range_should_give_3_for_numbers_below_5(self):
        self.assertEquals(find_totalOf_multiple_of_3_or_5_for_range(5), 3)

    def test_find_totalOf_multiple_of_3_or_5_for_range_should_give_8_for_numbers_below_6(self):
        self.assertEquals(find_totalOf_multiple_of_3_or_5_for_range(6), 8)


    def test_find_totalOf_multiple_of_3_or_5_for_range_should_give_minus_1_for_numbers_below_negative_number(self):
        self.assertEquals(find_totalOf_multiple_of_3_or_5_for_range(-3.3), -1)

    def test_find_totalOf_multiple_of_3_or_5_for_range_should_give_minus_1_for_numbers_below_float_number(self):
        self.assertEquals(find_totalOf_multiple_of_3_or_5_for_range(5.5), -1)
