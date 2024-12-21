with open("part-2_input.txt", "r") as file:
	big_line = ""
	for line in file:
		big_line += line


	i = 0
	result = 0
	do = True
	while (i < len(big_line)):
		if big_line[i:i+4] == "do()":
			do = True
		if big_line[i:i+7] == "don't()":
			do = False
		if big_line[i:i+4] == "mul(" and do == True:
			j = i + 4
			while big_line[j].isdigit():
				j += 1
			if big_line[j] == ',':
				j += 1
			while big_line[j].isdigit():
				j += 1
			if big_line[j] == ')':
				x, y = big_line[i:j+1].strip("mul()").split(",")
				result += (int(x) * int(y))
			i = j
		else:
			i += 1

print(result)