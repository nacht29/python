import inflect
import sys

inf = inflect.engine()

namelist = []
while True:
	try:
		name = input("Name: ").strip().capitalize()
	except EOFError:
		print("")
		break
	else:
		if name:
			namelist.append(name)

if not namelist:
	sys.exit()
print("Adieu, adieu to", inf.join(namelist))
