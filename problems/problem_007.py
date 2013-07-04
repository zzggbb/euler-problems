def isprime(n):
    n*=1.0
    for divisor in range(2,int(n**0.5)+1):
        if n/divisor==int(n/divisor):
            return False
    return True

def create_primes_list(max_index):
	global primes_list
	primes_list = []
	i = 2
	while len(primes_list) < max_index:
		if isprime(i):
			primes_list.append(i)
		i += 1
	return primes_list

