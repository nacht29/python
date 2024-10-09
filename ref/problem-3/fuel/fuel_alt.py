# Just some quality of life improvement
# The fundamentals did not change
# More user friendly by outputting errors

def main():
	x, y = get_fuel_fraction()
	print(calculate_fuel_percentage(x, y))


def get_fuel_fraction():
	while True:
		try:
			user_input = input("Fraction: ")
			x, y = user_input.split("/")
			x = int(x)
			y = int(y)
			if y == 0:
				print("Y cannot be 0. Please try again.")
				continue
			elif x > y:
				print("X cannot be greater than Y. Please try again.")
				continue
			return x, y
		except ValueError:
			print("Invalid input. Please enter integers separated by '/'.")
			continue


def calculate_fuel_percentage(x, y):
	result = (x / y) * 100
	if result >= 99:
		return "F"
	elif result <= 1:
		return "E"
	else:
		return f"{int(round(result))}%"


if __name__ == "__main__":
	main()
