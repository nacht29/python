with open("input.txt", "r") as file:
	big_line = ""
	for line in file:
		big_line += line

	i = 0
	result = 0
	while (i < len(big_line)):
		if big_line[i:i+4] == "mul(":
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