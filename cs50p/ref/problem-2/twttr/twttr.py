ip=input("Input: ")
output=""
vowels=['a','e','i','o','u']
for j in range(len(ip)):
	if ip[j].lower() not in vowels:
		output+=ip[j]
print("Output:",output)
