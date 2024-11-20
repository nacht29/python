def is_valid_coin(coin):
	return coin in [5, 10, 25]

def calculate_change(due):
	if due < 0:
		return abs(due)
	return 0

def main():
	due = 50
	accepted_coins = [5, 10, 25]

	while due > 0:
		print("Amount Due:", due)
		coin = int(input("Insert Coin: "))

		while not is_valid_coin(coin):
			print("Invalid coin. Accepted coins are 5, 10, and 25 cents.")
			coin = int(input("Insert Coin: "))

		due -= coin

	change_owed = calculate_change(due)
	if change_owed > 0:
		print("Change Owed:", change_owed)
	else:
		print("No change owed.")

if __name__ == "__main__":
	main()

'''
Improvements made:

1. Created separate functions for checking if the coin is valid and for calculating the change owed.

2. Used a while loop to keep prompting the user until the due amount becomes zero or negative.

3. Improved user feedback by providing an error message for invalid coins.

4. Encapsulated the main logic in a main() function to enhance modularity and readability.

5. Added a check to ensure that the program runs only when executed directly (not when imported as a module).
This is done by adding if __name__ == "__main__":.

These changes make the code more organized, easier to understand, and maintainable.
'''
