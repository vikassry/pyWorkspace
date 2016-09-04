import math
from datetime import datetime

def isPrime(number):
    if(number == 2):
        return True
    elif(number < 2 or number % 2 == 0 or int(number)!=number):
        return False
    max_sqrt = int(math.sqrt(number))+1
    for i in range(3, max_sqrt,2):
        if(number % i == 0):
            return False
    return True

# def find_prime_factors(number=600851475143):            #// not giving all prime factors for some numbers
#     prime_factors = []
#     for i in range(2, int(number**.5)+1):
#         if(isPrime(i) and (number % i == 0)):
#             prime_factors.append(i)
#     return prime_factors


def give_prime_numbers_upto(number):                    #// efficient and correct
    prime_numbers = [2]
    for n in range(3, number, 2):
        if isPrime(n):
            prime_numbers.append(n)
    return prime_numbers

def giveNextPrimeAt(x):
    return 1 + (x<<2) - ((x>>1)<< 1)

def generate_prime_factors_of(number):                      #// gives prime factors with duplicates
    max_sqrt = math.floor(math.sqrt(number))
    prime_index = 1
    current_prime = (number % 2 == 0) and 2 or 3
    while (current_prime <= max_sqrt) and (number % current_prime != 0):
        current_prime = giveNextPrimeAt(prime_index)
        prime_index += 1
    return (current_prime <= max_sqrt) and ([current_prime] + generate_prime_factors_of(number//current_prime)) or ([number])


def find_prime_factors_of(number=600851475143):         #// blazing fast for prime factors without duplicates
    if(number<=1):
        return []
    prime_factors = generate_prime_factors_of(number)
    uniq_prime_factors = sorted(set(prime_factors))
    return uniq_prime_factors


# start = datetime.now()
# print(find_prime_factors_of())
# print(datetime.now() - start)

# import cProfile
# import re
# cProfile.run('re.compile("print(find_prime_factors())")')
