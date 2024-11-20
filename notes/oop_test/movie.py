class Movie:
	def __init__(self, title, duration, price, seats):
		self.title = title
		self.duration = duration
		self.price = price
		self.seats = {row: [True] * 14 for row in "ABCDEFG"}

	def display_seats(self):
		print(f"\n{self.title} seat layout")
		for row, seats in self.seats.items():
			if (len(col) == 7):
				col.join(' ' * 5)
			col= ''.join('O' if taken else 'X' for taken in seats)
		print(f"{row}: {col}")
	
	def book(self, row, col):
		if self.seats[row][col - 1]:
			self.seats[row][col - 1] = False
			self.receipt(row, col)
		else:
			print("Sorry, the seat is taken.")
			return
	
	def receipt(self, row, col):
		print(f"Movie: {self.title}")
		print(f"Seat: {row}{col}")
