from domain.movie import Movie
from repository.in_memory_repository import InMemoryRepository
from service.movie_service import MovieService


class Console:
    repository = InMemoryRepository()
    movie_service = MovieService(repository)

    def __init__(self, movie_service):
        self.movie_service = movie_service

    def display_menu(self):
        print()
        print("MOVIE RENTAL SYSTEM")
        print("-" * 50)
        print("1. Movie Menu")
        print("2. Client Menu(to be implemented)")
        print("0. Exit")
        print()

    def display_movie_submenu(self):
        print()
        print("MOVIE MENU")
        print("-" * 50)
        print("1. Add Movie")
        print("2. View Movie")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("0. Back to Main Menu")
        print()

    def run(self):
        while True:
            self.display_menu()
            option = input("Enter your choice: ")
            if option == "1":
                self.run_movie_menu()
            elif option == "2":
                self.run_client_menu()
            elif option == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again")

    def run_movie_menu(self):
        while True:
            self.display_movie_submenu()
            option = input("Enter your choice: ")
            if option == "1":
                self.handle_add_movie()
            elif option == "2":
                self.handle_view_movie()
            elif option == "3":
                self.handle_update_movie()
            elif option == "4":
                self.handle_delete_movie()
            elif option == "0":
                break
            else:
                print("Invalid choice. Please try again")

    def handle_add_movie(self):
        print("---Add new Movie---")
        id = input("Enter the ID: ")
        title = input("Enter the title: ")
        year = input("Enter the year: ")
        genre = input("Enter the genre(ACTION, COMEDY, DRAMA, FANTASY, HORROR, MYSTERY, ROMANCE, THRILLER, WESTERN): ")
        age_restriction = input("Enter the age restriction(GA, PG, PG13, R, NC17): ")
        rental_price = input("Enter the rental price: ")
        available = input("Enter the availability(True/False): ")
        rent_counter = input("Enter the rent counter: ")

        new_movie = Movie(id, title, year, genre, age_restriction, rental_price, available, rent_counter)
        self.movie_service.save_movie(id, new_movie)

    def handle_view_movie(self):
        print("---View Movie---")
        id = input("Enter the movie ID: ")
        print(self.movie_service.read_movie(id))

    def handle_update_movie(self):
        print("---Update Movie---")
        id = input("Enter the movie ID: ")
        title = input("Enter the title: ")
        year = input("Enter the year: ")
        genre = input("Enter the genre(ACTION, COMEDY, DRAMA, FANTASY, HORROR, MYSTERY, ROMANCE, THRILLER, WESTERN): ")
        age_restriction = input("Enter the age restriction(GA, PG, PG13, R, NC17): ")
        rental_price = input("Enter the rental price: ")
        available = input("Enter the availability(True/False): ")
        rent_counter = input("Enter the rent counter: ")

        updated_movie = Movie(id, title, year, genre, age_restriction, rental_price, available, rent_counter)
        self.movie_service.update_movie(updated_movie)

    def handle_delete_movie(self):
        print("---Delete Movie---")
        id = input("Enter the movie ID: ")
        self.movie_service.delete_movie(id)

    def run_client_menu(self):
        pass



