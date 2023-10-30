from repository.in_memory_repository import InMemoryRepository
from service.movie_service import MovieService
from ui.console import Console


def main():
    movie_repository = InMemoryRepository()
    movie_service = MovieService(movie_repository)

    console = Console(movie_service)

    console.run()


if __name__ == "__main__":
    main()
