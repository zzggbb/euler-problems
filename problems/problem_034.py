# note: sum_factorial_digits() must be manually terminated

import math

def factorial_digits(number):
	sum = 0
	for i in str(number):
		sum += math.factorial(int(i))

	if sum == number:
		return True
	else:
		return False

def sum_factorial_digits():
	n = 3
	while True:
		if factorial_digits(n):
			print n
		n += 1
