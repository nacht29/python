def check_angles(big_line, row: int, col: int) -> int:
	angles = ["", "", "", "", "", ""]
	# 			top-right, top-left, bottom-left, bottom-right, up, down
	xmas = 0

	bound_row, bound_col = len(big_line), len(big_line[0])
	for i in range(4):
		if row - i >= 0 and col + i < bound_col:
			angles[0] += big_line[row - i][col + i]  # top-right
		if row - i >= 0 and col - i >= 0:
			angles[1] += big_line[row - i][col - i]  # top-left
		if row + i < bound_row and col - i >= 0:
			angles[2] += big_line[row + i][col - i]  # bottom-left
		if row + i < bound_row and col + i < bound_col:
			angles[3] += big_line[row + i][col + i]  # bottom-right
		if row - i >= 0:
			angles[4] += big_line[row - i][col] # up
		if row + i < bound_row:
			angles[5] += big_line[row + i][col] # down
	
	for line in angles:
		if line == "XMAS" or line == "SAMX":
			xmas += 1
	return (xmas)

with open("input.txt", "r") as file:
	big_line = [line.strip("\n") for line in file]

	xmas = 0
	for row in range(len(big_line)):
		for col in range(len(big_line[row])):
			if big_line[row][col] == 'X':
				if big_line[row][col:col+4] =="XMAS":
					xmas += 1
				'''since we are checking backwards, we need to make sure that
					there is enough space backwards to store SAMX'''
				if col >= 3 and big_line[row][col-3:col+1] == 'SAMX':
					xmas += 1
				xmas += check_angles(big_line, row, col)

	print(xmas)