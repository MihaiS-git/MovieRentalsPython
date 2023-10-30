from domain.BaseEntity import BaseEntity


class Movie(BaseEntity):
    MOVIE_GENRES = ("ACTION", "COMEDY", "DRAMA", "FANTASY", "HORROR", "MYSTERY",
                      "ROMANCE", "THRILLER", "WESTERN")
    AGE_RESTRICTIONS = ("GA", "PG", "PG13", "R", "NC17")

    def __init__(self, id, title, year, genre, age_restriction, rental_price, available, rent_counter):
        super().__init__(id)
        self.title = title
        self.year = year
        self.set_genre(genre)
        self.set_age_restriction(age_restriction)
        self.rental_price = rental_price
        self.available = available
        self.rent_counter = rent_counter

    def set_genre(self, genre):
        if genre in self.MOVIE_GENRES:
            self.genre = genre
        else:
            raise ValueError("Invalid genre")

    def set_age_restriction(self, age_restriction):
        if age_restriction in self.AGE_RESTRICTIONS:
            self.age_restriction = age_restriction
        else:
            raise ValueError("Invalid age restriction")

    def get_id(self):
        return self.id

    def __str__(self):
        return (f"Movie ID: {self.id}\nTitle: {self.title}\nYear: {self.year}\nGenre: {self.genre}\n"
                f"Age Restriction: {self.age_restriction}\nRentalPrice: {self.rental_price}\n"
                f"Available: {self.available}\nRent Counter: {self.rent_counter}")