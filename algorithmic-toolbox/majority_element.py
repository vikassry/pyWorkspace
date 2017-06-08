# Uses python3
import sys

# return 1 if a number occurs more than n/2 times in given list or returns -1 

def get_majority_element(a, left, right):
    if left == right:
        return -1
    number_count = {}
    
    for i in range(left, right):        
        number_count[a[i]] = number_count[a[i]]+1 if number_count.get(a[i]) != None else 1
    
    for count in number_count.values():
        if count > right/2:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
