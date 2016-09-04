
# ----------------------------------------------------------

# import math
# def generate_primes(n):
#         sqrtN = math.sqrt(n)
#         if n < 2:
#             return []
#         elif n < 3:
#             return [2]
#         primes = [2]
#         potentialPrimes = list(range(3,n+1,2))
#         currentPrime = potentialPrimes[0]

#         while currentPrime < sqrtN:
#             primes.append(currentPrime)
#             for i in potentialPrimes[:]:
#                 if i % currentPrime == 0:
#                     potentialPrimes.remove(i)
#             currentPrime = potentialPrimes[0]

#         primes += potentialPrimes
#         return primes

# def primeFactors(n):
#         sqrtn = int(math.sqrt(n))
#         primes = generate_primes(sqrtn)

#         factors = []
#         for i in primes:
#             if n % i == 0:
#             	factors.append(i)
#             	while n % i == 0:
#             		n //= i
#         if n != 1:
#             factors.append(n)

#         return factors

# print(primeFactors(input()))
# -----------------------------------------------------------

# def largestPrimeFactor(n):
#     factorList = []
# # Test for even
#     while (n % 2 == 0):
#         factorList.append(2)
#         n /= 2
# # Test for odd
#     i = 3
#     while (i < n**0.5): #if 3 is less than the square root of the even
#         while (n % i == 0):
#             factorList.append(i)
#             n /= i
#         i = i + 2
# # Test for other prime numbers
#     if n > 2:
#         factorList.append(n)

#     print(factorList)

# largestPrimeFactor(input())
#-----------------------------------------------------

# def getPrimeFactors(n):
#     return listFactors([n])

# def listFactors(input_list):
#     l = input_list
#     p = 2
#     while l[0] % p != 0:
#         p += 1
#     else:
#         if l[0] == p:
#             return l
#         else:
#             l[0] /= p
#             l.append(p)
#             return listFactors(l)

# print getPrimeFactors(600851475143)
# -----------------------------------------------------

# n = 600851475143
# i = 2
# while i * i < n:
#     while n % i == 0:
#         n = n / i
#     i = i + 1
# print n
#-----------------------------------------------------
