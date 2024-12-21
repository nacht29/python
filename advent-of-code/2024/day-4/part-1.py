def check_diagonals(big_line, row: int, col: int) -> int:
	diagonals = ["", "", "", ""]
	xmas = 0

	for i in range(4):
		diagonals[0] += (big_line[row - (i + 1)][col + (i + 1)])
		diagonals[1] += (big_line[row - (i + 1)][col - (i + 1)])
		diagonals[2] += (big_line[row + (i + 1)][col - (i + 1)])
		diagonals[3] += (big_line[row + (i + 1)][col + (i + 1)])
	
	for line in diagonals:
		if line == "XMAS" or line == "SMAX":
			xmas += 1
	return (xmas)

with open("part-1_input.txt", "r") as file:
	big_line = []
	for line in file:
		big_line.append(line)

	xmas = 0
	for row in range(len(big_line)):
		for col in range(len(big_line[row])):
			if big_line[row][col] == 'X':
				if big_line[row][col:col+4] =="XMAS":
					xmas += 1
				if big_line[row][col-3:4] == 'SMAX':
					xmas += 1
				xmas += check_diagonals(big_line, row, col)

	print(xmas)