# note: find_numbers() must be manually terminated

def digits_power(number, power):
	sum = 0
	for i in str(number):
		sum += (int(i) ** power)
	if sum == number:
		return True
	else:
		return False

def find_numbers(power):
	n = 2
	while True:
		if (digits_power(n, power)):
			print n
		n += 1
