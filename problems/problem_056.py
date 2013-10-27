def digital_sum(n):
	numbers = []
	for i in str(n):
		numbers.append(int(i))
	return sum(numbers)

with open('digital_sums.txt','w') as f:
	for a in range(100):
		for b in range(100):
			f.write(str(digital_sum(a ** b)) + "\n")