from collections import defaultdict

def main():
	grocery_list = []

	print("Enter items for the grocery list (Press Enter when done):")
	while True:
		item = input().strip().lower()
		if not item:
			break
		grocery_list.append(item)

	grocery_count = defaultdict(int)
	for item in grocery_list:
		grocery_count[item] += 1

	print("\nGrocery List:")
	for item, count in sorted(grocery_count.items()):
		print(f"{count} {item.capitalize()}")

if __name__ == "__main__":
	main()
