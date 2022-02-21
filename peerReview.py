'''System module'''
# Bradley Stenseth
# CIS245-T303
# Assignment 9.2

# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.)
# You need to identify the issues and correct them.

import random
import time

def display_intro():
	'''Displays the program intro'''
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight''')
	print()

def choose_cave():
	'''While loop to prompt for input to choose cave, requires 1 or 2'''
	cave = ''
	while cave not in('1', '2'):
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return cave

def check_cave(chosen_cave):
	'''Main program, randoms 1 or 2 and compares to choose_cave number'''
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendly_cave = random.randint(1, 2)

	if chosen_cave == str(friendly_cave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!')

play_again = 'yes'

while play_again in ('yes', 'y'):
	display_intro()
	caveNumber = choose_cave()
	check_cave(caveNumber)

	print('Do you want to play again? (yes or no)')
	play_again = input()
	if play_again == 'no':
		print('Thanks for planing')
