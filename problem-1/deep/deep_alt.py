def main():
	#strip whitespaces and lowercase
	usr = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

	#remove all digits, signs and symbols
	#remove excess spaces
	usr = process_str(usr)
	usr = " ".join(usr.split())

	pos_ans = ["42","forty two", "fortytwo"]
	print("Yes") if usr in pos_ans else print("No")

def process_str(usr):
	spec_char = "0123456789!@#$%^&*()_+~`:;<>,.?/\\\"\'"

	#list comprehension method
	# signs = [char for char in usr if char in spec_char]
	signs = [char for char in usr if char in spec_char]

	for rm in signs:
		usr = usr.replace(rm, "")
	return (usr)

if __name__ == '__main__':
	main()
