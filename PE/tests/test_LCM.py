from django.utils import unittest
from find_LCM import get_all_prime_factors_of_numbers_for_range, get_highest_power_for, find_lcm_for_range

__author__ = 'vikass'

class TestLcm(unittest.TestCase):

    def test_get_all_prime_factors_of_numbers_for_range_should_return_list_of_prime_fators_list(self):
        prime_factors_from_1_to_10 = [[1], [2], [3], [2, 2], [5], [2, 3], [7], [2, 2, 2], [3, 3], [2, 5]]
        self.assertListEqual(get_all_prime_factors_of_numbers_for_range(1,10), prime_factors_from_1_to_10)

    def test_get_all_prime_factors_of_numbers_for_range_should_return_list_of_prime_fators_list_for_0_and_1_with_themselves(self):
        self.assertListEqual(get_all_prime_factors_of_numbers_for_range(1,1),[[1]])
        self.assertListEqual(get_all_prime_factors_of_numbers_for_range(0,1),[[0],[1]])
        self.assertListEqual(get_all_prime_factors_of_numbers_for_range(0,3),[[0],[1],[2],[3]])

    def test_get_highest_power_for_should_return_3_for_prime_number_2_from_all_factors_from_1_to_10(self):
        all_factors = [[1],[2],[3],[2,2],[5],[2,3],[7],[2,2,2],[3,3],[2,5]]
        self.assertEqual(get_highest_power_for(2, all_factors), 3)

    def test_get_highest_power_for_should_return_1_for_prime_number_5_from_all_factors_from_1_to_10(self):
        all_factors = [[1],[2],[3],[2,2],[5],[2,3],[7],[2,2,2],[3,3],[2,5]]
        self.assertEqual(get_highest_power_for(5, all_factors), 1)

    def test_get_highest_power_for_should_return_0_for_prime_number_5_when_not_in_all_factors_list(self):
        all_factors = [[1],[2],[3],[2,2],[],[2,3],[7],[2,2,2],[3,3]]
        self.assertEquals(get_highest_power_for(5, all_factors), 0)

    def test_find_lcm_for_range_1_to_10_should_returns_lcm_2520(self):
        self.assertEqual(find_lcm_for_range(1,10), 2520)
        self.assertEqual(find_lcm_for_range(1,5), 60)

    def test_find_lcm_for_range_1_to_20_should_returns_lcm_232792560(self):
        self.assertEqual(find_lcm_for_range(1,20), 232792560)

    def test_find_lcm_for_range_for_same_start_and_end_should_returns_lcm_same_number(self):
        self.assertEqual(find_lcm_for_range(1,1), 1)
        self.assertEqual(find_lcm_for_range(3,3), 3)
        self.assertEqual(find_lcm_for_range(100,100), 100)
