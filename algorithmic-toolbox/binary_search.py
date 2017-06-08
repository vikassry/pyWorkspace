# Uses python3
import sys
from math import floor

def binary_search(a, x):
    return binarySearch(a, 0, len(a), x)

def binarySearch(a, low, high, val):
    if high < low:
        return -1
    mid = floor(low + (high - low)/2)
    
    if mid < 0 or mid >= len(a):
        return -1

    if val == a[mid]:
        return mid
    elif val < a[mid]:
        return binarySearch(a, low, mid-1, val)
    elif val > a[mid]:
        return binarySearch(a, mid+1, high, val)
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
