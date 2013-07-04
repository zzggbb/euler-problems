def pythagorean_triplet(sum):
	for a in range(1,sum+1):
		for b in range(1,sum+1):
			for c in range(1,sum+1):
				if (((a ** 2) + (b ** 2)) == (c ** 2)) and ((a + b + c) == sum):
					print a, b, c

pythagorean_triplet(1000)