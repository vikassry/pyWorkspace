def fibonacci(a, b, fib_array, number):
	if(a+b > number):
		return
	else:
		fib_array.append(a+b)
		return fibonacci(b, a+b, fib_array,number)

def get_fibonacci_series_till(number):
	a=0
	b=1
	fib_series = []
	if isinstance(number, float):
		return fib_series
	elif(number==1):
		return [b]
	fibonacci(a,b, fib_series, number)
	return fib_series

def get_sum_of_even_number_of_fibonacci_series_till(number):
	fiboonacci_series = get_fibonacci_series_till(number)
	total = sum([ fiboonacci_series[i] for i in range(1,len(fiboonacci_series)) if fiboonacci_series[i] % 2 == 0])
	return total

# print(get_sum_of_even_number_of_fibonacci_series_till(4000000))
