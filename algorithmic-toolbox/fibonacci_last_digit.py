# Uses python3
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous, current  = 0, 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
