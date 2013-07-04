def getpassed(min,max):
    passed = 0
    number = max
    while passed != 20:
	    for i in range(min,(max + 1)):
	        if number % i == 0:
	            passed = passed + 1
	        #elif number % i != 0:
	    	else:
	            number = number + 1
	            passed = 0

    print ("The number " + str(number) + " is the lowest number"
    	   "divisible by all numbers from " + str(min) + " to " + str(max))