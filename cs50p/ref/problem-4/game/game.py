from random import randint

while True:
	try:
		level=int(input("Level: "))
		if level <=0:
			raise ValueError
		break
	except ValueError:
		continue

rand=randint(1,level)

while True:
	try:
		guess=int(input("Guess: "))
	except ValueError:
		continue
	else:
		if guess==rand:
			print("Just right!")
			break
		elif guess<rand:
			print("Too small!")
		elif guess>rand:
			print("Too large!")
