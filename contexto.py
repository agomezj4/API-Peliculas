class Context:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movies(self):
        return self.movies

    def get_movie_by_id(self, id):
        for movie in self.movies:
            if movie.id == id:
                return movie
        return None

    def get_movies_by_category(self, category):
        return [movie for movie in self.movies if movie.category == category]