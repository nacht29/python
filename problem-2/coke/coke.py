def get_int(prompt):
	while True:
		try:
			num = int(input(prompt))
		except ValueError:
			continue
		else:
			return num

# only accepts 25, 10, and 5 cents
# returns 0 if any other int is given
# the coin will not be deducted from Amount Due, loop continues
def insert_coin():
	acceptable = [25, 10, 5]
	coin = get_int("Insert Coin: ")
	if coin in acceptable:
		return coin
	else:
		return 0

# always print Amount Due
# loop breaks when Amount Due <= 0
# prints Changed Owed, 0 is counted also
due = 50
while True:
	print("Amount Due:", due)
	coin = insert_coin()
	due -= coin
	if due <= 0:
		print("Change Owed:", due * -1)
		break
