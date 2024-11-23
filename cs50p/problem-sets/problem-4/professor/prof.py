from random import randint
from cs50p.lib import get_int

def main():
	upper_lim = get_upper_limit()
	base, x, y = generate_integer(upper_lim)
	game(base, x, y)

def get_upper_limit():
	while True:
		level = get_int("Level: ")
		if level >= 1:
			break

	limit = 0
	for i in range(level):
		limit = limit * 10 + 9

	return (limit)

# 99 / 9 = 11 (1 time) | base = 1 * 10 = 10 -> limit(base, cap) = limit(10, 99)
def generate_integer(upper_lim):
	base = 1
	cap = upper_lim

	while (upper_lim > 111):
		base *= 10
		upper_lim = upper_lim / 9

	x = randint(base, cap)
	y = randint(base, cap)
	return base, x, y

def game(base, x, y):
	comp = x + y
	attempts = base
	score = 0

	while attempts:
		for i in range (3):
			try:
				player = int(input(f"{x} + {y} = "))
			except ValueError:
				print("EEE")
				continue
			else:
				if (player == comp):
					score += 1
					break
				elif i == 2:
					print(f"{x} + {y} =", comp)
		attempts -= 1
	print("Score:", score)

if __name__ == '__main__':
	main()
