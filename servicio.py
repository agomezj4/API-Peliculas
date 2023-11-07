from repositorio import MovieRepository

class MovieService:
    def __init__(self):
        self.repository = MovieRepository()

    def add_movie(self, id, title, overview, year, rating, category):
        self.repository.add_movie(id, title, overview, year, rating, category)

    def get_movies(self):
        return self.repository.get_movies()

    def get_movie_by_id(self, id):
        return self.repository.get_movie_by_id(id)

    def get_movies_by_category(self, category):
        return self.repository.get_movies_by_category(category)