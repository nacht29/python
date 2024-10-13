def format_date(months):
	while True:
		date = input("Date: ")
		# for the case of mm/dd/yyyy
		if '/' in date:
			# tries to split into exactly 3 varaibles
			# will result in ValueError if there are extra stuff
			try:
				
				mm, dd, yy = date.replace(' ', '').split('/')
				mm = int(mm)
				dd = int(dd)
				yy = int(yy)
			except ValueError:
				continue
		# for the case of September 8, 1616 format
		else:
			# tries to split into exactly 3 varaibles
			# will result in ValueError if there are extra stuff
			try:
				mm, dd, yy = date.split()
				# gets the corresponding int val for a month from the [months] dict
				mm = months[mm]
				dd = int(dd.replace(',', ''))
				yy = int(yy)
			except ValueError:
				continue

		if (valid_date(mm, dd, yy) == True):
			return (f"{yy}-{mm}-{dd}")
			break
		else:
			continue


def valid_date(mm, dd, yy):
	big_month = [1, 3, 5, 7, 8, 10, 12]
	small_month = [4, 6, 9, 11]
	if mm < 0 or mm > 12:
		return False
	if (dd < 0):
		return False
	if mm in big_month and dd > 31:
		return False
	if mm in small_month and dd > 30:
		return False
	if mm == 2:
		if yy % 4 == 0 and dd > 29:
			return False
		elif yy % 4 != 0 and dd > 28:
			return False
	return True

mon = [ "January", "February", "March", "April", "May", "June", "July", 
	   "August", "September", "October", "November", "December"]

months = {}
for i in range(len(mon)):
	months[mon[i]] = i + 1

date = format_date(months)
print(date)
