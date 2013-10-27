def lychrel(n):
	iters = 1
	current = n
	current = current + int(str(current)[::-1])

	while not (int(str(current)[::-1]) == current) and iters < 50:
		current = current + int(str(current)[::-1])
		iters += 1

	return iters == 50

def lychrels_below(limit):
	found = 0
	for i in range(limit):
		if lychrel(i):
			found += 1

	return found

print lychrels_below(input("Give a number: "))