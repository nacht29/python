def main():
	dollars = dollars_to_float(input("How much was the meal? "))
	percent = percent_to_float(input("What percentage would you like to tip? "))
	tip = dollars * percent
	print(dollars, percent)
	print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
	# Remove any dollar sign and convert directly to float
	d = d.replace("$", "")
	return float(d)

def percent_to_float(p):
	# Remove any percentage sign and convert directly to float, dividing by 100
	p = p.replace("%", "")
	return float(p) / 100

if __name__ == '__main__':
	main()
