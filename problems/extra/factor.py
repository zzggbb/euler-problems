def factors(n):
	factors = []
	for i in range(1,n/2):
		if n % i == 0:
			factors.append(i)
	return factors

print factors(100)