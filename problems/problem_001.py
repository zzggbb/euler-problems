def sum_of_multiples(mult_1, mult_2, max):
	total_sum = 0
	for i in range(0,(max)):
		if (i % mult_1 == 0 or i % mult_2 == 0):
			total_sum += i
	print total_sum

sum_of_multiples(input("First Multiple: "), input("Second Multiple: "), input("Maximum: "))
