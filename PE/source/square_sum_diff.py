
def get_square_of_sum_numbers_in_range(start, end):
	return sum([i for i in range(start, end+1)])**2

def get_sum_of_squares_in_range(start, end):
	return sum([i**2 for i in range(start, end+1)])

def get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range(start, end):
	return (get_square_of_sum_numbers_in_range(start, end) - get_sum_of_squares_in_range(start, end))

# print(get_difference_of_square_of_sum_of_numbers_and_sum_of_squares_of_numbers_in_range(1,100))