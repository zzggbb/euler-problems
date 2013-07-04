def palindrome(digits):
	min_digit = 10 ** (digits - 1)
	max_digit = (10 ** (digits)) - 1
	palindromes = []
	for a in range(min_digit,max_digit + 1):
		for b in range(min_digit,max_digit + 1):
			palindrome = str(a * b)
			if palindrome == palindrome[::-1]:
				palindromes.append(int(palindrome))
	print max(palindromes)
