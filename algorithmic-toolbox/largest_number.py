#Uses python3
from functools import cmp_to_key

def my_sort (x, y):
	if len(x) == len(y):
		if x < y:
			return 1
		return -1

	if len(x) > len(y):
		if x.find(y) == 0:
			return 1
		if x[0] < y[0]:
			return -1
		return -1

	if len(x) < len(y):
		if y.find(x) == 0:
			return 1
		if x[0] < y[0]:
			return 1
		return -1

	return 0


def largest_number(numbers):
	# sorted_list = sorted(numbers, key=itemgetter(0), reverse=True)
	sorted_list = sorted(numbers, key=cmp_to_key(my_sort))
	return "".join(sorted_list)


if __name__ == '__main__':
    n = int(input())
    # data = [ int(x) for x in input().split() ]
    data = input().split()
    print(largest_number(data))
