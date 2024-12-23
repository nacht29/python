with open("input.txt", "r") as file:
	big_line = [line.strip("\n") for line in file]

	xmas = 0
	bound_row, bound_col = len(big_line), len(big_line[0])
	for row in range(len(big_line)):
		# l1  - top-right to bottom-left
		l1, l2 = "", ""
		for col in range(len(big_line[row])):
			if big_line[row][col] == 'A':
				## l1
				if row - 1 >= 0 and col + 1 < bound_col: # top right
					l1 = big_line[row - 1][col + 1]
				l1 += 'A'
				if row + 1 < bound_row and col - 1 >= 0: # bottom left
					l1 += big_line[row + 1][col - 1]
				## l2##
				if row - 1 >= 0 and col - 1 >= 0: # top left
					l2 = big_line[row - 1][col - 1]
				l2 += 'A'
				if row + 1 < bound_row and col + 1 < bound_col: # bottom right
					l2 += big_line[row + 1][col + 1]

				if (l1 == "MAS" or l1 == "SAM") and (l2 == "MAS" or l2 == "SAM"):
					xmas += 1
	print(xmas)