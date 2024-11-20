# updates grocery list
# add new item and set count to 1
# else, add 1 to item count if item alr exists
def update_list(grocery, item):
	if item in grocery:
		grocery[item] += 1
	else:
		grocery[item] = 1
	# return grocery

grocery = {}
while True:
	try:
		item = input().strip().upper()
		update_list(grocery, item)
	except EOFError:
		print()
		for i in grocery:
			print(grocery[i], i)
		break
