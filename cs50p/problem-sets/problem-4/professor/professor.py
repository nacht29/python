from random import randint
from cs50p.lib import get_int

def main():
	upper_lim = get_upper_limit()
	lower_lim = get_lower_limit(upper_lim)
	game(lower_lim, upper_lim)

def get_upper_limit():
	while True:
		level = get_int("Level: ")
		if level >= 1:
			break

	upper_lim = 0
	for i in range(level):
		upper_lim = upper_lim * 10 + 9

	return (upper_lim)

def get_lower_limit(upper_lim):
	lower_lim = 1

	while (lower_lim * 10 < upper_lim):
		lower_lim *= 10

	return (lower_lim)

def game(lower_lim, upper_lim):
	score = 0

	for i in range(10):
		x = randint(lower_lim, upper_lim)
		y = randint(lower_lim, upper_lim)
		for j in range(3):
			try:
				player = int(input(f"{x} + {y} = "))
			except ValueError:
				print("EEE")
				continue
			else:
				if (player == x + y):
					score += 1
					break
				elif (j == 2):
					print(f"{x} + {y} =", x + y)
				else:
					print("EEE")
	print("Score:", score)

if __name__ == '__main__':
	main()