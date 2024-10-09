def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")

def is_valid(s):
	if s.isalnum() == False or len(s) > 6  or len(s) < 2:
		return False
	i = 0
	# iterates thru alpha
	while s[i].isalpha() == True:
		i += 1
	# check if there are at least 2 alpha
	if (i < 2 and len(s) > 2) or (len(s) == 2 and s[1].isalpha == False):
		return False
	# i stops at the first non-alpha aka first digit
	# returns False if it is 0
	if (s[i] == '0'):
		return False
	# return True if i manage to reach end of s
	# must do it this way to avoid IndexError
	while s[i].isdigit() == True:
		if (i == len(s) - 1):
			return True
		i += 1
	# this means i didn't manage to reach the end of s
	return False

if __name__ == '__main__':
	main()