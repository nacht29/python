file = open("puzzle.txt", "r")

left = []
right = []
for line in file:
	parts = line.split()
	left.append(int(parts[0]))
	right.append(int(parts[1]))

left.sort()
right.sort()

result = 0
for i in range(len(left)):
	for j in range(len(right)):
		if right[j] == left[i]:
			result += right[j]

print(result)