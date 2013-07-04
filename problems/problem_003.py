def largest_prime(number):
	i = 2
	while i * i < number:
		while number % i == 0:
			number = number / i
		i += 1
	print number