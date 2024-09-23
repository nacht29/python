camel = input("camelCase: ")
snake = ""

for i in range(len(camel)):
	if camel[i].isupper() and i != 0:  # Skip the first character
		snake += "_" + camel[i].lower()
	else:
		snake += camel[i]

print("snake_case:", snake)
