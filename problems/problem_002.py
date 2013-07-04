import sys

def nth_fibonacci(n):
	a,b = 0,1
	for i in range(0,n):
		a,b = b,a+b
	return a

def even_sum_fibonacci(max):
	sum = 0
	n = 1
	while (nth_fibonacci(n) < max):
		if nth_fibonacci(n) % 2 == 0:
			sum = sum + nth_fibonacci(n)
		n += 1
	print sum