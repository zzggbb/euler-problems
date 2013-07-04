# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @ Name:        collatz_prob14.py
# @ Purpose:     provide useful modules to experiment with the Collatz Conjecture          
# @ Author:      hifi / Arez
# @ Created:     June 24, 2013
#-------------------------------------------------------------------------------

import sys

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


def most_steps_in_range(exclusive_end):
	record_steps = 0
	for number in range(1, exclusive_end):
		total_steps = collatz(number,0)
		if total_steps > record_steps:
			record_steps = total_steps
			record_number = number
	print "In the range of 1 and %s, the number that resulted in the most steps was %s with %s steps!" % (str(exclusive_end), str(record_number), str(record_steps))


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


def log_number_steps(value_list):
	values_log = open('collatz_number_steps.txt','a')

	for index in range(0,len(value_list)):
		x_coord = value_list[index][0]
		y_coord = value_list[index][1]
	values_log.write(str(value_list) + "\n")


def option_menu():
	while True:
		print "Options:"
		print "\t1: Find the number of steps for a given starting number."
		print "\t2: Find the number, in a given range, that results in the most steps."
		print "\t3: Create a list with x = \'given number\' and y = \'total steps\'"
		print "\t4: Create a list-log file of given numbers and total steps"
		print "\t5: Exit"

		user_answer = input("What would you like to do?\n")

		if user_answer == 1:
			collatz(input("Type a starting number: "),1)
		elif user_answer == 2:
			most_steps_in_range(input("Give an exclusive ending range! "))
		elif user_answer == 3:
			steps_in_range(input("Give an exclusive ending range! "),1)
		elif user_answer == 4:
			log_number_steps(steps_in_range(input("Given an exclusive ending range! "),0))
		elif user_answer == 5:
			sys.exit()
		else:
			print "Sorry, I didn't understand that!"

if __name__ == '__main__':
	option_menu()
