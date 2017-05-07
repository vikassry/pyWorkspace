# Uses python3

n = int(input())
numbers = [ int(x) for x in input().split() ]
assert(len(numbers) == n)

def get_two_largest_numbers(numbers):
	max_index1 = -1
	max_index2 = -1

	for i in range(0, len(numbers)):
		if max_index1 == -1 or numbers[i] > numbers[max_index1]:
			max_index1 = i

	for j in range(0, len(numbers)):
	    if (j != max_index1) and (max_index2 == -1 or numbers[j] >= numbers[max_index2]):
	        max_index2 = j

	return numbers[max_index2], numbers[max_index1]

num1, num2 = get_two_largest_numbers(numbers)

print(num1 * num2)
