import csv

from config.config import MOVIES_CSV_FILE
from domain.movie import Movie
from repository.in_memory_repository import InMemoryRepository


class InFileRepository(InMemoryRepository):
    movies_csv_file = MOVIES_CSV_FILE

    def __init__(self, movies_csv_file):
        super().__init__()
        self.movies_csv_file = movies_csv_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.movies_csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header
                for row in reader:
                    id, title, year, genre, age_restriction, rental_price, available, rent_counter = row
                    movie = Movie(id, title, year, genre, age_restriction, rental_price, available, rent_counter)
                    self.data[id] = movie
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading data from CSV: {str(e)}")

    def save_all_to_file(self):
        try:
            with open(self.movies_csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Title", "Year", "Genre", "AgeRestriction",
                                 "RentalPrice", "Available", "RentCounter"])
                for movie in self.data.values():
                    writer.writerow([
                        movie.get_id(),
                        movie.get_title(),
                        movie.get_year(),
                        movie.get_genre(),
                        movie.get_age_restriction(),
                        movie.get_rental_price(),
                        movie.is_available(),
                        movie.get_rent_counter()
                    ])
        except Exception as e:
            print(f"Error saving data to CSV: {str(e)}")

    def save(self, id, movie):
        if not movie.get_id() in self.data.keys():
            self.data[movie.get_id()] = movie
            self.save_all_to_file()
        else:
            print(f"There is already a Movie with ID {movie.get_id()} in the repository")

    def update(self, id, movie):
        if movie.get_id() in self.data.keys():
            self.data[movie.get_id()] = movie
            self.save_all_to_file()
        else:
            print(f"Movie with ID {movie.get_id()} not found in the repository")

    def delete(self, id):
        if id in self.data.keys():
            del self.data[id]
            self.save_all_to_file()
        else:
            print(f"Movie with ID {id} not found in the repository")
