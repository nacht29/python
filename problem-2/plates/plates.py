import math
def main():
	plate = input("Plate: ").strip().upper()
	if is_valid(plate)==True:
		print("Valid")
	elif is_valid(plate)==False:
		print("Invalid")

def is_valid(s):
	sc="^[@_!#$%^&*()<>?}{~:;',.]"
	sc2=['"',"'",'/','\\','|']
	if s[0:1].isalpha()==False or len(s)<2 or len(s)>6:
		return False
	elif position(s)==False:
		return False
	else:
		for i in range(len(s)):
			if s[i-1] in sc or s[i-1] in sc2:
				return False
			else:
				return True

def position(s):
	l=len(s)
	check=(l+1)/2
	check=math.floor(check)
	if s[check-1].isalpha()==False:
		return False
	for i in range(l-1):
		if s[i].isalpha() and s[i+1].isalpha()==False:
			if s[i+1]=='0':
				return False
main()
