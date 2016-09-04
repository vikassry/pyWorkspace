from django.utils import unittest
from fibonacci import fibonacci, get_fibonacci_series_till, get_sum_of_even_number_of_fibonacci_series_till

__author__ = 'vikass'

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_makes_fibonacci_series_till_13_for_number_20_with_intial_values_1_2(self):
        fibonacci_series = [1,2]
        fibonacci(1,2,fibonacci_series,20)
        self.assertListEqual(fibonacci_series, [1,2,3,5,8,13])

    def test_fibonacci_makes_list_with_3_for_till_3_with_intial_values_1_2(self):
        fibonacci_series = []
        fibonacci(1,2,fibonacci_series,3)
        self.assertListEqual(fibonacci_series, [3])

    def test_fibonacci_doesnt_add_anything_to_fib_series_till_2_with_intial_values_1_2(self):
        fibonacci_series = []
        fibonacci(1,2,fibonacci_series,2)
        self.assertListEqual(fibonacci_series, [])

    def test_fibonacci_makes_fibonacci_series_till_13_till_20_with_intial_values_0_1(self):
        fibonacci_series = []
        fibonacci(0,1,fibonacci_series,20)
        self.assertListEqual(fibonacci_series, [1,2,3,5,8,13])

    def test_fibonacci_makes_fibonacci_series_for_decimal_number(self):
        fibonacci_series = []
        fibonacci(0,1,fibonacci_series,20.4)
        self.assertListEqual(fibonacci_series, [1,2,3,5,8,13])

    def test_fibonacci_doesnt_add_anything_to_fibonacci_series_when_negative_number_is_given(self):
        fibonacci_series = [1,2]
        fibonacci(1,2,fibonacci_series, -12)
        self.assertListEqual(fibonacci_series, [1,2])

    def test_get_fibonacci_series_till_10_gives_list_untill_value_8(self):
        self.assertListEqual(get_fibonacci_series_till(10),[1,2,3,5,8])

    def test_get_fibonacci_series_till_negative_number_gives_empty_list(self):
        self.assertListEqual(get_fibonacci_series_till(-1),[])

    def test_get_fibonacci_series_till_0_gives_empty_list(self):
        self.assertListEqual(get_fibonacci_series_till(0),[])

    def test_get_fibonacci_series_till_1_gives_list_with_1(self):
        self.assertListEqual(get_fibonacci_series_till(1),[1])

    def test_get_fibonacci_series_till_2_gives_list_with_1_2(self):
        self.assertListEqual(get_fibonacci_series_till(2),[1,2])

    def test_get_fibonacci_series_till_decimal_number_gives_empty_list_(self):
        self.assertListEqual(get_fibonacci_series_till(2.42),[])

    def test_get_sum_of_even_number_of_fibonacci_series_till_50_gives_44(self):
        self.assertEquals(get_sum_of_even_number_of_fibonacci_series_till(50), 44)

    def test_get_sum_of_even_number_of_fibonacci_series_till_10_gives_4613732(self):
        self.assertEquals(get_sum_of_even_number_of_fibonacci_series_till(4000000), 4613732)

    def test_get_sum_of_even_number_of_fibonacci_series_till_negative_number_gives_0(self):
        self.assertEquals(get_sum_of_even_number_of_fibonacci_series_till(-1), 0)

    def test_get_sum_of_even_number_of_fibonacci_series_till_decimal_number_gives_0(self):
        self.assertEquals(get_sum_of_even_number_of_fibonacci_series_till(50.0), 0)
