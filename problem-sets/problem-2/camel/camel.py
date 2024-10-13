camel = input("camelCase: ")
snake = ""

for i in range(len(camel)):
	if camel[i].isupper() and i != 0:  # Skip the first character
		snake += "_" + camel[i].lower()
	else:
		snake += camel[i]

print("snake_case:", snake)

'''
# Previous solution
camel = input("camelCase: ")
snake = ""
for i in range(len(camel) - 1):
	snake += camel[i].lower()
	if (camel[i + 1].isupper() == True):
		snake += '_'
snake += camel[len(camel) - 1].lower()
print("snake_case:", snake)
'''
