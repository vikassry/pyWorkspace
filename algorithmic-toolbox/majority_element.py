# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    number_count = {}
    for i in range(left+1, right):        
        number_count[a[i]] = number_count[a[i]] + 1 if number_count.get(a[i])!=None else 1

    print(number_count)
    for count in number_count.values():
        if count > 1:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
    