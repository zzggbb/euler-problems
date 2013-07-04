def factorial(n): #100
	sum = 1
	for i in range(0,n): #0,1,2,3...99
		sum = sum * (n-i)
	return sum

def sum_factorial_digits(n):
	sum = 0
	for i in str(factorial(n)):
		sum += int(i)
	return sum

print sum_factorial_digits(100)