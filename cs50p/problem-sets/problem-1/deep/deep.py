def main():
	#strip whitespaces and lowercase
	usr = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

	#remove all digits, signs and symbols
	#remove excess spaces
	usr = process_str(usr)
	usr = " ".join(usr.split())

	pos_ans = ["42","forty two", "fortytwo"]
	if usr in pos_ans:
		print ("Yes")
	else:
		print("No")

def process_str(usr):
	signs = []
	spec_char = "0123456789!@#$%^&*()_+~`:;<>,.?/\\\"\'"

	#for loop can be simplified in list comprehension
	# signs = [char for char in usr if char in spec_char]
	for char in usr:
		if char in spec_char:
			signs.append(char)

	for rm in signs:
		usr = usr.replace(rm, "")
	return (usr)

if __name__ == '__main__':
	main()
