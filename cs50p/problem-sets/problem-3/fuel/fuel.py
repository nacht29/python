def main():
	x, y = get_frac()
	calc_fuel(x, y)

def get_frac():
	while True:
		try:
			frac = input("Fraction: ")
			x, y = frac.split('/')
			x = int(x)
			y = int(y)
		except ValueError:
			continue
		else:
			if (x > y):
				get_frac()
			return x, y
		
def calc_fuel(x, y):
	fuel  = x / y * 100
	if (fuel > 99):
		print('F')
	elif (fuel < 1):
		print('E')
	else:
		print(f"{int(round(fuel,0))}%") # to remove the .0 at the tail

if __name__ == '__main__':
	main()
