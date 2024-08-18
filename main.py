from controller.controller import MovieController
from model.model import Movie
from view.view import MovieView

# Создаем экземпляр фильма
movie = Movie(
    title="Finding Nemo",
    genre="Animation, Adventure",
    director="Andrew Stanton",
    release_year=2003,
    duration="100 minutes",
    studio="Pixar Animation Studios"
)

# Создаем контроллер для фильма
controller = MovieController(movie)

# Создаем представление для отображения информации
view = MovieView(controller)

# Показываем информацию о фильме
view.show_information()

# Добавляем актеров
view.add_actor("Albert Brooks", "Marlin")
view.add_actor("Ellen DeGeneres", "Dory")

# Показываем обновленную информацию о фильме
view.show_information()