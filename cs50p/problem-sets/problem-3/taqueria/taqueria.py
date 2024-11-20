# returns price of grocery item if found
def update_cost(grocery) -> int:
	item = input("Item: ").title()
	item = " ".join(item.split())
	for in_stock in grocery:
		if in_stock == item:
			return grocery[in_stock]

grocery = {
	"Baja Taco": 4.25,
	"Burrito": 7.50,
	"Bowl": 8.50,
	"Nachos": 11.00,
	"Quesadilla": 8.50,
	"Super Burrito": 8.50,
	"Super Quesadilla": 9.50,
	"Taco": 3.00,
	"Tortilla Salad": 8.00
}

price = 0
while True:
	try:
		price += update_cost(grocery)
	except TypeError:
		continue
	except EOFError:
		print()
		break
	else:
		print(f"Total: ${price:.2f}")
