'''
this problem assumes user input will be in the format of x y z
where x = num1
	  y = expression (+, -, *, /)
	  z = num2
'''

'''
retrieve non-space -> only the important part of the expression is kept
Espression: -1 + 1
> ["-1", " ", "+", " ", "1"]
> ["-1", "+", "1"]
'''
usr = input("Expression: ")
usr = usr.split()
exp_list = [exp for exp in usr if exp != " "]
x = int(exp_list[0])
z = int(exp_list[2])
match exp_list[1]:
	case "+":
		print(round(x + z, 1))
	case "-":
		print(round(x - z, 1))
	case "*":
		print(round(x * z, 1))
	case "/":
		print(round(x / z, 1))

