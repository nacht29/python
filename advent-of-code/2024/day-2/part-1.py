with open("input.txt", "r") as file:
	safe_count = 0
	for line in file:
		num = line.split()
		if len(num) < 2:
			continue
		constant = int(num[0]) - int(num[1])
		if not (-3 <= constant <= 3):
			continue
		safe = True
		for i in range(len(num) - 1):
			result = int(num[i]) - int(num[i + 1])
			if not (-3 <= result <= 3) or result == 0 or (constant > 0 and result < 0) or (constant < 0 and result > 0):
				safe = False
				break
		if safe == True:
			safe_count += 1

print(safe_count)