'''
LIST METHODS
'''

# list comprehension 

def process_str(usr):
	spec_char = "0123456789!@#$%^&*()_+~`:;<>,.?/\\\"\'"

	#list comprehension method
	# signs = [char for char in usr if char in spec_char]
	signs = [char for char in usr if char in spec_char]

# is the same as 

def process_str(usr):
	signs = []
	spec_char = "0123456789!@#$%^&*()_+~`:;<>,.?/\\\"\'"

	for char in usr:
		if char in spec_char:
			signs.append(char)
