def main():
	x,y=check()
	print(calculate(x,y))


def check():
	while True:
		try:
			user=input("Fraction: ")
			x,y=user.split("/")
			x=int(x)
			y=int(y)
		except ValueError:
			pass
		else:
			if int(x)>int(y) or y=='0':
				user=input("Fraction: ")
			return int(x),int(y)

def calculate(x,y):
	try:
		result=(x/y)*100
	except ValueError:
		check()
	else:
		if result>=99:
			return "F"
		elif result<=1:
			return "E"
		else:
			return f"{int(round(result,0))}%"

if __name__ == '__main__':
		main()