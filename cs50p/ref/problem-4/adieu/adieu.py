import inflect

def get_names():
	names = []
	while True:
		try:
			name = input("Name: ")
			names.append(name.strip())
		except EOFError:
			break
	return names

def farewell(names):
	p = inflect.engine()
	if len(names) == 0:
		print("No names provided.")
	elif len(names) == 1:
		print(f"Adieu, adieu, to {names[0]}")
	elif len(names) == 2:
		print(f"Adieu, adieu, to {names[0]} and {names[1]}")
	else:
		farewell_string = ", ".join(names[:-1]) + ", and " + names[-1]
		print(f"Adieu, adieu, to {farewell_string}")

def main():
	names = get_names()
	farewell(names)

if __name__ == "__main__":
	main()
