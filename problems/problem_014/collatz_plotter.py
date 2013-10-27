import numpy as np
import matplotlib.pyplot as plt
from ast import literal_eval

def collatz(n, context):
	i = 0
	steps_list = []
	while n != 1:
		if (n % 2 == 0):
			n = n / 2
			i+=1
			if context == 1:
				print str(n) + "\n"
			if context == 2:
				steps_list.append(n)
		else:
			n = (3 * n) + 1
			i+=1
			if context == 1:
				print str(n) + "\n"
			if context == 2:
				steps_list.append(n)

	if context == 1:
		print "Reached 1 in " + str(i) + " steps!"
	if context == 0:
		return i

def steps_in_range(exclusive_end, context):
	number_steps_list = []

	for number in range(1, exclusive_end):
		total_steps = collatz(number,0)
		#						  x-coord, y-coord
		number_steps_list.append((number,total_steps))
	if context == 1:
		print number_steps_list
	if context == 0:
		return number_steps_list

def plotter():

	data = steps_in_range(100000001,0)

	X = [x for (x,y) in data]
	Y = [y for (x,y) in data]

	plt.plot(X,Y)
	plt.axis([0,1000,0,300])
	plt.xlabel( "Input Values" )
	plt.ylabel( "Steps to One" )
	plt.show()

plotter()