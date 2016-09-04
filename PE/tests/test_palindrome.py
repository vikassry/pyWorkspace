import unittest
from largest_palindrome import is_palindrome, give_largest_palindrome_numbers_for_product_of_digit

__author__ = 'vikass'

class TestPalindromeNumber(unittest.TestCase):
    def test_is_palindrome_should_return_True_for_palindrome_number_121(self):
        self.assertTrue(is_palindrome(121))

    def test_is_palindrome_should_return_True_for_single_digit_number(self):
        self.assertTrue(is_palindrome(2))
        self.assertTrue(is_palindrome(0))

    def test_is_palindrome_should_return_False_for_123(self):
        self.assertFalse(is_palindrome(123))

    def test_give_largest_palindrome_numbers_for_product_of_digit_should_return_9_for_1_digit(self):
        self.assertEquals(give_largest_palindrome_numbers_for_product_of_digit(1), 9)

    def test_give_largest_palindrome_numbers_for_product_of_digit_should_return_9009_for_2_digit(self):
        self.assertEquals(give_largest_palindrome_numbers_for_product_of_digit(2), 9009)

    def test_give_largest_palindrome_numbers_for_product_of_digit_should_return_906609_for_3_digit(self):
        self.assertEquals(give_largest_palindrome_numbers_for_product_of_digit(3), 906609)

    # def test_give_largest_palindrome_numbers_for_product_of_digit_should_return_99000099_for_4_digit(self):
    #     self.assertEquals(give_largest_palindrome_numbers_for_product_of_digit(4), 99000099)