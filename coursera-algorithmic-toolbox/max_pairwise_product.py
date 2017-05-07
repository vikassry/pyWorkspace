# Uses python3
from functools import reduce

n = int(input())
numbers = [ int(x) for x in input().split() ]
assert(len(numbers) == n)

def get_two_largest_numbers(numbers):
	max_index = -1
	largest_number = reduce(lambda x,y: x if(x>y) else y, numbers)
	for i in range(0, len(numbers)):
	    if (numbers[i]!=largest_number) and (max_index == -1 or numbers[i] > numbers[max_index]):
	        max_index = i
	return numbers[max_index], largest_number

num1, num2 = get_two_largest_numbers(numbers)

print(num1 * num2)
