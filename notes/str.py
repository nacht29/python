'''
STRING METHODS
'''

# print on a single line
print("hello", end = "")
print("world")

# splits strings into substrings
name = input("name: ")
str_arr = []
str_arr = name.split(" ")
print(str_arr)

## FORMATING ##

#formatting floats 
while (1):
	try:
		flt = float(input("float: "))
	except ValueError:
		continue
	else:
		break
print(f"{flt:,.2f}")

'''
This syntax is combining two features of pattern matching:

Capture patterns: case name
Guard clauses: if name in gryf

The full syntax case <pattern> if <guard>: allows you to specify both a pattern to match and an additional condition that must be met.
In your specific example:

The pattern name will match any value (since it's just a variable name with no constraints).
The guard if name in gryf adds the condition that this matched value must be in the gryf list.
'''
gryf = ["Harry", "Ron", "Hermione"]
slyt = ["Draco", "Crabbe", "Goyle"]
search = input("name: ")
match search:
	case search if search in gryf:
		print("Gryffindor")
	case search if search in slyt:
		print("Slytherin")
	case _:
		print("Not found in any house")

# remove excess spaces
expression = input("Expression: ").lower().split()
expression = " ".join(expression.split())

# isalnum check
string = "12345 hello world"
print(string.replace(' ', '').isalnum())
print(string)
