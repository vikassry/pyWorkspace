import math

def is_palindrome(number):
	num = number
	reverse_number = 0
	remainder = math.floor(num % 10)
	while num > 0:
		remainder = math.floor(num % 10)
		num = math.floor(num / 10)
		reverse_number = (reverse_number * 10 + remainder)
	return int(reverse_number)==int(number)


def give_largest_palindrome_numbers_for_product_of_digit(digit):
	if(digit==1):
		return 9
	start = 8 * pow(10, digit-1)
	end = pow(10,digit)
	palindrome_numbers = []
	for i in range(start,end):
		for j in range(start,end):
			product = i * j
			is_palindrome(product) and palindrome_numbers.append(product)
	return max(palindrome_numbers)


# print(give_largest_palindrome_numbers_for_product_of_digit(3))