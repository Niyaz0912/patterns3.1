class MovieController:
    def __init__(self, movie):
        self.movie = movie

    def get_information(self):
        return self.movie.get_information()

    def add_actor(self, name, role):
        self.movie.add_actor(name, role)