from django.utils import unittest
from get_Nth_prime_number import givePrimeAt
from prime_factors import isPrime, find_prime_factors_of, give_prime_numbers_upto, giveNextPrimeAt, \
    generate_prime_factors_of

__author__ = 'vikass'


class TestPrimeNumberLibrary(unittest.TestCase):
    def test_isPrime_returns_True_for_2(self):
        self.assertTrue(isPrime(2))

    def test_isPrime_returns_False_for_0(self):
        self.assertFalse(isPrime(0))

    def test_isPrime_returns_False_for_1(self):
        self.assertFalse(isPrime(1))

    def test_isPrime_returns_False_for_negative_number(self):
        self.assertFalse(isPrime(-1))

    def test_isPrime_returns_True_for_104743(self):
        self.assertTrue(isPrime(104743))

    def test_isPrime_returns_False_for_35_and_81(self):
        self.assertFalse(isPrime(35))
        self.assertFalse(isPrime(81))

    def test_isPrime_returns_True_for_prime_number(self):
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(103))
        self.assertTrue(isPrime(6857))

    def test_isPrime_returns_False_for_any_even_number_greater_than_2(self):
        self.assertFalse(isPrime(4))
        self.assertFalse(isPrime(100))
        self.assertFalse(isPrime(12345678908))

    def test_give_prime_numbers_upto_should_give_list_of_prime_factors(self):
        self.assertListEqual(give_prime_numbers_upto(10), [2,3,5,7])
        self.assertListEqual(give_prime_numbers_upto(50), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])

    def test_giveNextPrimeAt_should_return_5_for_1_and_7_for_2(self):
        self.assertEquals(giveNextPrimeAt(1), 5)
        self.assertEquals(giveNextPrimeAt(2), 7)

    def test_giveNextPrimeAt_should_return_1_for_0(self):
        self.assertEquals(giveNextPrimeAt(0), 1)

    def test_giveNextPrimeAt_should_return_minus_1_for_minus_1(self):
        self.assertEquals(giveNextPrimeAt(-1), -1)
        self.assertEquals(giveNextPrimeAt(-8), -23)

    def test_giveNextPrimeAt_should_return_35_for_11_which_is_wrong_but_this_method_is_supposed_to_give_prime_candidates_also(self):
        self.assertEquals(giveNextPrimeAt(11), 35)
        self.assertEquals(giveNextPrimeAt(8), 25)

    def test_givePrimeNumberAt_should_return_37_for_11and_19_for_index_8(self):
        self.assertEquals(givePrimeAt(11), 31)
        self.assertEquals(givePrimeAt(8), 19)

    def test_generate_prime_factors_should_return_prime_factors_for_1234567890(self):
        self.assertListEqual(generate_prime_factors_of(1234567890), [2,3,3,5,3607,3803])

    def test_generate_prime_factors_should_return_list_with_tht_number_when_its_prime_number_or_0_or_1(self):
        self.assertListEqual(generate_prime_factors_of(0), [0])
        self.assertListEqual(generate_prime_factors_of(2), [2])
        self.assertListEqual(generate_prime_factors_of(3), [3])
        self.assertListEqual(generate_prime_factors_of(6857), [6857])

    def test_find_prime_factors_of_return_list_with__2_for_2(self):
        self.assertListEqual(find_prime_factors_of(4), [2])
        self.assertListEqual(find_prime_factors_of(100), [2,5])

    def test_find_prime_factors_of_should_return_empty_list_for_prime_number_itself(self):
        self.assertListEqual(find_prime_factors_of(2), [2])
        self.assertListEqual(find_prime_factors_of(101), [101])

    def test_find_prime_factors_of_should_return_empty_list_for_1(self):
        self.assertListEqual(find_prime_factors_of(1), [])

    def test_find_prime_factors_of_should_return_empty_list_for_0(self):
        self.assertListEqual(find_prime_factors_of(0), [])

    def test_find_prime_factors_of_should_return_empty_list_for_negative_number(self):
        self.assertListEqual(find_prime_factors_of(-2), [])

    def test_generate_prime_factors_should_return_unique_prime_factors_for_1234567890(self):
        self.assertListEqual(find_prime_factors_of(1234567890), [2,3,5,3607,3803])

    def test_find_prime_factors_of_return_list_for_600851475143(self):
        self.assertListEqual(find_prime_factors_of(600851475143), [71,839,1471,6857])

    def test_givePrimeAt_should_return_104743_for_index_10001(self):
        self.assertEquals(givePrimeAt(10001), 104743)

    def test_givePrimeAt_should_return_2_3for_index_1_2(self):
        self.assertEquals(givePrimeAt(1), 2)
        self.assertEquals(givePrimeAt(2), 3)

    def test_givePrimeAt_should_return_minus_1_for_negative_index(self):
        self.assertEquals(givePrimeAt(-1), -1)

    def test_givePrimeAt_should_return_minus_1_for_0_index(self):
        self.assertEquals(givePrimeAt(0), -1)

    def test_givePrimeAt_should_return_minus_1_for_decimal_index(self):
        self.assertEquals(givePrimeAt(4.5), -1)
