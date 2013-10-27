def d(n):
	const = ""
	for i in range(n):
		const+=str(i)
	return int(const[n])

prod = 1
for i in range(7):
    prod = prod * d(10 ** i)

print prod