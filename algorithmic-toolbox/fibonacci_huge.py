# Uses python3
def get_fibonacci_huge_naive(number, m):
    n = number % 60             # Since last digit of fibonacci series follow a pattern after first 60 last digits
    numbersToAdd = 60 if (number > 60) else 0
    if n <= 1:
        return n

    previous = 0
    current  = 1
    for _ in range(n - 1 + numbersToAdd):
        previous, current = current, (previous + current)
        print(current%m)

    return current % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))

"""
0 0 0
1 1 1
2 1 2
3 2 4
4 3 7
5 5 12
6 8 20
7 13 33
8 21 54
9 34 88
10 55 143
""" 