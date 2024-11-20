def get_int(prompt):
	while True:
		try:
			val = int(input(prompt))
		except ValueError:
			continue
		else:
			return (val)

def get_float(prompt):
	while True:
		try:
			val = float(input(prompt))
		except ValueError:
			continue
		else:
			return (val)

def get_str(prompt):
	while (True):
		s = input(prompt)
		if s.isalpha():
			return s
		else:
			continue