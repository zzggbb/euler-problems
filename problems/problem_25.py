def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def n_digit_fib(digit_length):
	n = 1
	while len(str(fib(n))) < digit_length:
		 n = n + 1
	print n