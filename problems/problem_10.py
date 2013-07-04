def is_prime(num):
    for i in range( 2, int(num ** 0.5) + 1 ):
        if (num % i) == 0:
            return False
    return True

def sum_primes(max):
	sum = 0
	for i in range(2,max):
		if is_prime(i):
			sum += i
	print sum