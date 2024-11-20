greet = input("Greeting: ").lower().strip()

if (greet == ""):
	print("$100")

else:
	greet = greet.split()
	if (greet[0] == "hello"):
		print("$0")
	elif (greet[0][0] == 'h' and greet[0] != "hello"):
		print("$20")
	else:
		print("$100")