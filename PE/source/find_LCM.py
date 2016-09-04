from prime_factors import generate_prime_factors_of, give_prime_numbers_upto
from functools import reduce

def get_all_prime_factors_of_numbers_for_range(start, limit):
	return [generate_prime_factors_of(x) for x in range(start, limit+1)]

def get_highest_power_for(prime, primes_list):
	highest_power = 0
	for primes in primes_list:
		count = primes.count(prime)
		highest_power = highest_power<= count and count or highest_power
	return highest_power

def find_lcm_for_range(start, end):
	if start == end:
		return start
	lcm_dividers = []
	prime_numbers = give_prime_numbers_upto(end+1)
	all_prime_factors = get_all_prime_factors_of_numbers_for_range(start, end)
	
	for prime in prime_numbers:
		highest_number_of_factor = get_highest_power_for(prime, all_prime_factors)
		lcm_dividers.append(prime ** highest_number_of_factor)
	return reduce(lambda x,y : x * y, lcm_dividers)

# print(find_lcm_for_range(1, 20))