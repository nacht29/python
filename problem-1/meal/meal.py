def main():
	time = input("What time is it? ")
	time = convert(time)
	if (time == -1):
		print("Invalid time")
	elif (7 < time < 8):
		print("breakfast time")
	elif (12 < time < 13):
		print("lunch time")
	elif (18 < time < 19):
		print("dinner time")

def convert(time):
	hr, mnt = time.split(':')
	if (mnt[0] >= '6'):
		return (-1)
	dec_time = float(hr) + (float(mnt) / 60)
	return(round(dec_time, 1))

if __name__ == "__main__":
	main()