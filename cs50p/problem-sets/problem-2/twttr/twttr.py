usr = input("Input: ")
out = ""
vowels = ['a', 'e', 'i', 'o', 'u',
		  'A', 'E', 'I', 'O', 'U']
for c in usr:
	if c not in vowels:
		out += c
		
print("Output:", out)
