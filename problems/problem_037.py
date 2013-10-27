def is_prime(n):
    for x in xrange(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def is_left_truncatable(n): #3797
	score = 0
	for i in range(len(str(n))): #0,1,2,3
		if is_prime(int(str(n)[i::])):
			score += 1
	if score == len(str(n)):
		return True
	return False