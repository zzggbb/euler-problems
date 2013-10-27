def self_powers(beg,end):
	sum = 0
	for x in range(beg, (end + 1)):
		sum += (x ** x)
	return sum

print self_powers(1,1000)