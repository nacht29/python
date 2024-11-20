ask=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
match ask.lower().strip():
	case "forty-two" | "forty two" |  "42":
		print("Yes")
	case _:
		print("No")

#Alternate solution with loops (Just to clarify, I have some very basic knowledge in Python)
'''
truth='N'
while truth=='N':
	ask=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
	match ask.lower().strip():
		case "fourty-two" | "fourty two" |  "42":
			print("Yes")
			truth='Y'
		case _:
			print("No")
			quit=input("Do you wish to continue another time? [Y/N] ")
			match quit:
				case "Y" | "N":
					truth=quit
				case _:
					quit=input("Do you wish to continue another time? [Y/N] ")
'''
