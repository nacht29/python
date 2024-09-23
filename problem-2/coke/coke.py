def isnumber(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

due=50
accepted=[5,10,25]
while True :
	if due>0:
		print("Amount Due:",due)
	elif due<=0:
		if due==0:
			print("Change Owed: 0")
		elif due<0:
			print("Change Owed:",due*-1)
		break
	coin=input("Insert Coin: ")
	while isnumber(coin)==False or int(coin) not in accepted:
		print("Amount Due:",due)
		coin=input("Insert Coin: ")
	due-=int(coin)
