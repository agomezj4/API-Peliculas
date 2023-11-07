from contexto import Context
from modelo import Movie

class MovieRepository:
    def __init__(self):
        self.context = Context()

    def add_movie(self, id, title, overview, year, rating, category):
        movie = Movie(id, title, overview, year, rating, category)
        self.context.add_movie(movie)

    def get_movies(self):
        return self.context.get_movies()

    def get_movie_by_id(self, id):
        return self.context.get_movie_by_id(id)

    def get_movies_by_category(self, category):
        return self.context.get_movies_by_category(category)