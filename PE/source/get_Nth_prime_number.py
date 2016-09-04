from prime_factors import giveNextPrimeAt, isPrime
from datetime import datetime

def givePrimeAt(index=100001): 		#// my first simple algorithm
	if(index<1 or isinstance(index, float)):
		return -1
	if index == 1:
		return 2
	prime_numbers =[2,3]
	i = 1
	while len(prime_numbers) < index:
		prime_number = giveNextPrimeAt(i)
		isPrime(prime_number) and prime_numbers.append(prime_number)
		i += 1
	return prime_numbers[index-1]



def getNthPrime(N=100001): 					#//another as efficient as above
	if N == 1:
		return 2
	index, primeNumber = 1,3
	while index < N:
		if isPrime(primeNumber):
			index += 1
		primeNumber += 2
	return primeNumber - 2


# start = datetime.now()
# print(givePrimeAt())
# print (datetime.now() - start)
