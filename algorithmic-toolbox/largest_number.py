#Uses python3
from operator import itemgetter

def largest_number(numbers):
	sorted_list = sorted(numbers, key=itemgetter(0), reverse=True)
	return "".join(sorted_list)


if __name__ == '__main__':
    n = int(input())
    # data = [ int(x) for x in input().split() ]
    data = input().split()
    print(largest_number(data))
