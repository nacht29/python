greet = input("Greeting: ").lower().strip()
if (greet == ""):
	print("$100")
elif (greet[0:5] == "hello"):
	print("$0")
elif (greet[0] == 'h' and greet[0:4] != "hello"):
	print("$20")
else:
	print("$100")