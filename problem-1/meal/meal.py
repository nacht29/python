def main():
	ct=input("What time is it? ")
	if 7<=convert(ct)<=8:
		print("breakfast time")
	elif 12<=convert(ct)<=13:
		print("lunch time")
	elif 18<=convert(ct)<=19:
		print("dinner time")

def convert(time):
	hr,min=time.split(":")
	new_min=float(min)/60
	new_time=(float(hr)+new_min)
	return new_time

if __name__ == "__main__":
	main()
