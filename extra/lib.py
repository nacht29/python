# default get_int
def get_int(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			continue # or pass

# get integer with customisable err msg output
def get_int_err(prompt, err_msg):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print(err_msg)
			continue # or pass