def check_diagonals(big_line, row: int, col: int) -> int:
	diagonals = ["", "", "", ""]
	xmas = 0

	bound_row, bound_col = len(big_line), len(big_line[0])
	for i in range(4):
		if row - i >= 0 and col + i < bound_col:
			diagonals[0] += big_line[row - i][col + i]  # Top-right
		if row - i >= 0 and col - i >= 0:
			diagonals[1] += big_line[row - i][col - i]  # Top-left
		if row + i < bound_row and col - i >= 0:
			diagonals[2] += big_line[row + i][col - i]  # Bottom-left
		if row + i < bound_row and col + i < bound_col:
			diagonals[3] += big_line[row + i][col + i]  # Bottom-right
	
	for line in diagonals:
		if line == "XMAS" or line == "SMAX":
			xmas += 1
	return (xmas)

with open("part-1_input.txt", "r") as file:
	big_line = [line.strip("\n") for line in file]

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