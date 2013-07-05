def sum_digits(base,power):
	sum = 0
	for i in (str(base ** power)):
		sum += int(i)
	return sum