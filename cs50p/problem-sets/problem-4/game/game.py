from random import randint
from cs50p.lib import get_int
from sys import exit

while True:
	level = get_int("Level: ")
	if (level >= 1):
		break

comp = randint(1, level)
while True:
	player = get_int("Guess: ")
	if (player == comp):
		print("Just right!")
		exit()
	elif player < comp:
		print("Too small!")
	else:
		print("Too large!")
