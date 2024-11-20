class Movie:
	def __init__(self, title, duration, price):
		self.title = title
		self.duration = duration
		self.price = price
		self.seats = {row: [True] * 10 for row in 'ABCDEFG'}

	def display_seats(self):
		print(f"\nSeat availability for '{self.title}':")
		for row, seats in self.seats.items():
			seat_row = ''.join('O' if taken else 'X' for taken in seats)
			print(f"{row}: {seat_row}")

	def book_seat(self, row, seat_number):
		if self.seats[row][seat_number - 1]:
			self.seats[row][seat_number - 1] = False
			print(f"Seat {row}{seat_number} successfully booked for '{self.title}'.")
			return self.price
		else:
			print(f"Seat {row}{seat_number} is already booked!")
			return 0


class Cinema:
	def __init__(self, name):
		self.name = name
		self.movies = []

	def add_movie(self, movie):
		self.movies.append(movie)

	def display_movies(self):
		print(f"\nMovies available at {self.name}:")
		for idx, movie in enumerate(self.movies, start=1):
			print(f"{idx}. {movie.title} ({movie.duration} min) - ${movie.price:.2f}")

	def select_movie(self, movie_index):
		if 0 < movie_index <= len(self.movies):
			return self.movies[movie_index - 1]
		else:
			print("Invalid selection. Try again!")
			return None


# Example usage
if __name__ == "__main__":
	# Create a cinema
	my_cinema = Cinema("Grand Movie Theatre")

	# Add some movies
	movie1 = Movie("Inception", 148, 10.0)
	movie2 = Movie("The Matrix", 136, 8.5)
	movie3 = Movie("Interstellar", 169, 12.0)

	my_cinema.add_movie(movie1)
	my_cinema.add_movie(movie2)
	my_cinema.add_movie(movie3)

	# Interact with the system
	while True:
		my_cinema.display_movies()
		choice = input("\nEnter the number of the movie to view seats or 'q' to quit: ")
		if choice.lower() == 'q':
			print("Exiting the system. Thank you!")
			break
		elif choice.isdigit():
			movie = my_cinema.select_movie(int(choice))
			if movie:
				movie.display_seats()
				book = input("\nDo you want to book a seat? (y/n): ").lower()
				if book == 'y':
					row = input("Enter the row (A-G): ").upper()
					seat = int(input("Enter the seat number (1-10): "))
					movie.book_seat(row, seat)
