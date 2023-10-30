from repository.in_memory_repository import InMemoryRepository


class MovieService:
    repository = InMemoryRepository()

    def __init__(self, repository):
        self.repository = repository

    def save_movie(self, id, movie):
        self.repository.create(id, movie)

    def read_movie(self, id):
        return self.repository.read(id)

    def update_movie(self, movie):
        self.repository.update(movie.get_id(), movie)

    def delete_movie(self, id):
        self.repository.delete(id)
