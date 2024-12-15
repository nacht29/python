file = open("puzzle.txt", "r")

left = []
right = []
for line in file:
	parts = line.split()
	left.append(int(parts[0]))
	right.append(int(parts[1]))

left.sort()
right.sort()

result  = 0
for i in range(len(left)):
	if left[i] >= right[i]:
		result += left[i] - right[i]
	else:
		result += right[i] - left[i]

print(result)