from config.config import MOVIES_CSV_FILE
from repository.in_file_repository import InFileRepository


class MovieService:
    repository = InFileRepository(MOVIES_CSV_FILE)

    def __init__(self, repository):
        self.repository = repository

    def save_movie(self, id, movie):
        self.repository.save(id, movie)

    def read_movie(self, id):
        return self.repository.read(id)

    def update_movie(self, movie):
        self.repository.update(movie.get_id(), movie)

    def delete_movie(self, id):
        self.repository.delete(id)
