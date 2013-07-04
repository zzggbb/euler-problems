def squares_difference(maximum):
	sum_of_squares = 0
	sum_of_nums = 0
	for i in range(1,(maximum + 1)):
		sum_of_squares+=(i ** 2)
		sum_of_nums+=i
	print ((sum_of_nums ** 2) - sum_of_squares)
