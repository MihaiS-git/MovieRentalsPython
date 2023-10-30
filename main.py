from config.config import MOVIES_CSV_FILE
from repository.in_file_repository import InFileRepository
from service.movie_service import MovieService
from ui.console import Console


def main():
    movie_repository = InFileRepository(MOVIES_CSV_FILE)
    movie_service = MovieService(movie_repository)

    console = Console(movie_service)

    console.run()


if __name__ == "__main__":
    main()
