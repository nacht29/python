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


'''
LIST METHODS
'''

# list comprehension 

def process_str(usr):
	spec_char = "0123456789!@#$%^&*()_+~`:;<>,.?/\\\"\'"

	#list comprehension method
	# signs = [char for char in usr if char in spec_char]
	signs = [char for char in usr if char in spec_char]

# is the same as 

def process_str(usr):
	signs = []
	spec_char = "0123456789!@#$%^&*()_+~`:;<>,.?/\\\"\'"

	for char in usr:
		if char in spec_char:
			signs.append(char)

'''
DICTIONARIES
'''
# finding a key among a list of dicts
students = [
	{"name": "Chan", "age": 18},
	{"name": "Yeo", "age": 18}
]

find = "Chan"
for search in students:
	if search["name"] == find:
		print(search)
		# this is how you format the output
		print(search["name"], search["age"], sep = ',')

# finding one key from a single dict
ppl = {
	"Her": 18,
	"Ron": 18,
}
# for loop iterates thru the keys
# hence, search means the key
# ppl[search] prints out the value of key
find = "He"
for search in ppl:
	if find == search:
		print(search, ppl[search])
# one interesting trick:
# this also return an output because He is a substr of Her
# hence, He is in Her
find = "He"
for search in ppl:
	if find in search:
		print(search, ppl[search])
