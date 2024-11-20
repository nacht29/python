def calculate(expression):
	try:
		result = eval(expression)
		return result
	except Exception as e:
		return f"Error: {str(e)}"

while True:
	expression = input("Enter an arithmetic expression (or 'quit' to exit): ")
	if expression.lower() == 'quit':
		break
	else:
		result = calculate(expression)
		print("Output:", result)
