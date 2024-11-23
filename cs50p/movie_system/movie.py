import cs50p.lib as lib
import sys

class Movie:
	def __init__(self, title, duration, price):
		self.title = title
		self.duration = duration
		self.price = price
		self.seats = {row: [True] * 14 for row in "ABCDEFG"}

	def display_seats(self):
		print(f"\n{self.title} seat layout")
		for row, seats in self.seats.items():
			col = ''.join('O' if taken else 'X' for taken in seats)
			col = col[:7] + (' ' * 5) + col[:7]
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

class Cinema:
	def __init__(self, name):
		self.name = name
		self.movie_db = []

	def login(self):
		while True:
			try:
				print("\nLogin page:\n1. Staff\n2. Customer\n3. Exit")
				login = input("Login (1/2/3): ")
			except EOFError:
				sys.exit()
			except KeyboardInterrupt:
				sys.exit()
			else:
				if (login == "1"):
					self.staff()
					break
				elif (login == "2"):
					self.customer()
				elif (login == '3'):
					sys.exit("Logged out successfully")

	def logout(self):
		while True:
			try:
				logout = input("\nLog out (y/n): ")
			except EOFError:
				print()
				self.logout()
			except KeyboardInterrupt:
				sys.exit()
			else:
				if (logout.strip().lower() == 'y'):
					self.login()
				elif (logout.strip().lower() == 'n'):
					break
				else:
					continue
	
	'''
	for row in movie.seats
		for seat in row
			any(seat) - return True if there is a True value
	'''
	def show_movies(self):
		title = "*On theatre*"
		print(f"\n{'_' * len(title)}")
		print("\n*On theatre*")
		print(f"\n{'_' * len(title)}")

		for idx, movie in enumerate(self.movie_db, start = 1):
			print(f"\n{idx}. {movie.title} ({movie.duration} min) - ${movie.price:.2f}")
			
			available = any(seat for row in movie.seats.values() for seat in row)
			print("Available") if available else print("Unavailable")
				

	def staff(self):
		while True:
			print("\nAction:\n1. Add movie to db\n2. Show movie db\n3. Log out")
			try:
				action = input("\nAction: ")
			except EOFError:
				print()
				self.logout()
			except KeyboardInterrupt:
				break
			else:
				if (action == '1'):
					self.staff_add_movie()
				elif (action.strip() == '2'):
					self.show_movies()
				elif (action.strip() == '3'):
					self.logout()

	def staff_add_movie(self):
		while True:
			try:
				title = input("Title: ")
				duration = lib.get_int("Duration (min): ")
				price = lib.get_float("Price: ")
			except EOFError:
				print()
				break
			except KeyboardInterrupt:
				break
			else:
				movie = Movie(title, duration, price)
				self.movie_db.append(movie)

	def customer(self):
		print("Log out for now")
		self.logout()