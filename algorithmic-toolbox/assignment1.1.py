# Uses python3

n = int(input())
numbers = [ int(x) for x in input().split() ]
assert(len(numbers) == n)

def get_two_largest_numbers(numbers):
	largest_number , second_largest_number = 0, 0

	for i in range(0, len(numbers)):
		if numbers[i] > largest_number:
			second_largest_number = largest_number
			largest_number = numbers[i]
		elif numbers[i] > second_largest_number:
			second_largest_number = numbers[i]

	return largest_number, second_largest_number

num1, num2 = get_two_largest_numbers(numbers)

print(num1 * num2)
