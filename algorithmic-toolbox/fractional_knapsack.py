# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	max_value = 0
	value_per_weight = tuple(zip(values, weights))
	sorted_knapsack = sorted(value_per_weight, key=lambda tup: tup[0]/tup[1], reverse=True)

	for i in range(0, len(weights)):
		if capacity == 0:
			return max_value
		max_unit = sorted_knapsack[i]
		current_weight = min(capacity, max_unit[1])
		capacity -= current_weight
		max_value = max_value + current_weight * max_unit[0]/max_unit[1]

	return max_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
