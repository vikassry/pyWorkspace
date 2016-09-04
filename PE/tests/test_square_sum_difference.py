from django.utils import unittest
from square_sum_diff import get_square_of_sum_numbers_in_range, get_sum_of_squares_in_range, \
    get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range

__author__ = 'vikass'

class TestSquareSumDifference(unittest.TestCase):

    def test_get_square_of_sum_of_range_should_return_1_for_range_1_to_1(self):
        self.assertEquals(get_square_of_sum_numbers_in_range(1,1), 1)

    def test_get_square_of_sum_of_range_should_return_36_for_range_1_to_3(self):
        self.assertEquals(get_square_of_sum_numbers_in_range(1,3), 36)

    def test_get_square_of_sum_of_range_should_return_0_for_range_0_to_0(self):
        self.assertEquals(get_square_of_sum_numbers_in_range(0,0), 0)

    def test_get_square_of_sum_of_range_should_return_3025_for_range_1_to_10(self):
        self.assertEquals(get_square_of_sum_numbers_in_range(1,10), 3025)

    def test_get_square_of_sum_of_range_should_return_3025_for_range_negative_10_to_negative_1(self):
        self.assertEquals(get_square_of_sum_numbers_in_range(-10,-1), 3025)

    def test_get_sum_of_squares_in_range_should_return_total_of_all_squares_of_numbers_in_given_range(self):
        self.assertEquals(get_sum_of_squares_in_range(1,10), 385)

    def test_get_sum_of_squares_in_range_should_return_45_for_range_1_to_5(self):
        self.assertEquals(get_sum_of_squares_in_range(1,5), 55)

    def test_get_sum_of_squares_in_range_should_return_385_for_range_negative_10_to_negative_1(self):
        self.assertEquals(get_sum_of_squares_in_range(-10,-1), 385)

    def test_get_sum_of_squares_in_range_should_return_1_for_range_0_to_1(self):
        self.assertEquals(get_sum_of_squares_in_range(0,1), 1)

    def test_get_sum_of_squares_in_range_should_return_0_for_range_0_to_0(self):
        self.assertEquals(get_sum_of_squares_in_range(0,0), 0)

    def test_get_sum_of_squares_in_range_should_return_25_for_range_5_to_5(self):
        self.assertEquals(get_sum_of_squares_in_range(5,5), 25)
        self.assertEquals(get_sum_of_squares_in_range(4,5), 41)

    def test_get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range_1_to_5_should_return_170(self):
        self.assertEquals(get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range(1,5),170)

    def test_get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range_1_to_10_should_return_2640(self):
        self.assertEquals(get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range(1,10),2640)

    def test_get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range_negative_10_to_negative_1_should_return_2640(self):
        self.assertEquals(get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range(-10,-1),2640)

    def test_get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range_1_to_100_should_return_24164150(self):
        self.assertEquals(get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range(1,100),25164150)