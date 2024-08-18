class Movie:
    def __init__(self, title, genre, director, release_year, duration, studio):
        self.title = title
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.duration = duration
        self.studio = studio
        self.actors = []  # Список для хранения актеров и их ролей

    def add_actor(self, name, role):
        self.actors.append({"Name": name, "Role": role})

    def get_information(self):
        information = {
            "Title": self.title,
            "Genre": self.genre,
            "Director": self.director,
            "Release Year": self.release_year,
            "Duration": self.duration,
            "Studio": self.studio,
            "Actors": self.actors,
        }
        return information
