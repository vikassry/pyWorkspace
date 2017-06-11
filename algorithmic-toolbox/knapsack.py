# Uses python3
import sys

def knapsack(W, weights):
	n = len(weights)
	values = [[0 for x in range(W+1)] for x in range(n+1)]

	for i in range(n+1):
		for w in range(W+1):
			if i==0 or w==0:
				values[i][w] = 0
			elif weights[i-1] <= w:
				values[i][w] = max(weights[i-1] + values[i-1][w-weights[i-1]],  values[i-1][w])
			else:
				values[i][w] = values[i-1][w]
	return values[n][W]

if __name__ == '__main__':
	input = sys.stdin.read()
	W, n, *weights = list(map(int, input.split()))
	print(knapsack(W, weights))
