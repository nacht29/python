import sys

def valid_update(manual: list[int], median: list[str]) -> tuple[bool, int]:
	for i in range(len(median) - 1):
		comb = median[i] + '|' + median[i + 1]
		found_valid_comb = False
		# loops and checks manual to see if any valid pair matches current pair
		# if valid, move on to the next pair
		for valid_comb in manual:
			if comb == valid_comb:
				found_valid_comb = True
				break
		# if current pair is invalid, return False immediately
		if not found_valid_comb:
			return (False, i)
	# return True if every combination in this prticular str (update) is correct
	return (True, i)

def rearrange(manual: list[int], median: list[str], idx: int) -> list[str]:
	temp = median[idx + 1]
	median[idx + 1] = median[idx]
	median[idx] = temp
	return (median)

with open(sys.argv[1], "r") as input_file:
	file = input_file.readlines()

	#line != "\n" to exclude adding empty lines
	manual = [line.split("\n")[0] for line in file if '|' in line and line != "\n"]
	updates = [line.split("\n")[0] for line in file if not ('|' in line) and line != "\n"]

	corrected_median = 0
	count = False
	for update in updates:
		median = update.split(",")

		while (True):
			is_valid_update, idx = valid_update(manual, median)
			if not is_valid_update:
				median = rearrange(manual, median, idx)
				count = True
			else:
				break

		if count:
			corrected_median += int(median[(len(median) - 1) // 2])
			count = False
	
	print(corrected_median)
			