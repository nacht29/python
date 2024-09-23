m = int(input("m: "))
print("E:", m*((3*(10**8))**2))

#with error handling (I learned this few years ago when I was self-learning Python and doing mini projects)
''''
def isfloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

m = input("m: ")
while isfloat(m) == False:
	m = input("m: ")
print("E:", int(m)*((3*(10**8))**2))
'''
