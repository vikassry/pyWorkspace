# Uses python3
def fibonacci_sum_naive(number):
    n = number % 60             # Since last digit of fibonacci series follow a pattern after first 60 last digits
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1 + 60):     # this worked because sum of repeating 60 last digits is zero.
        previous, current = current, (previous + current) % 10
        sum += current

    return sum % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_naive(n))
