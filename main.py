from controller.controller import MovieController
from model.model import Movie
from view.view import MovieView

# Создаем экземпляр фильма
movie = Movie(
    title="Области тьмы",
    genre="Фантастика",
    director="Нил Бёргер",
    release_year=2011,
    duration="105 минут",
    studio="Relativity Media, Virgin Produced"
)

# Создаем контроллер для фильма
controller = MovieController(movie)

# Создаем представление для отображения информации
view = MovieView(controller)

# Показываем информацию о фильме
view.show_information()

# Добавляем актеров
view.add_actor("Бредли Купер", "Эдди Морра")
view.add_actor("Роберт Де Ниро", "Карл Ван Лун")
view.add_actor("Эбби Корниш", "Линди")
view.add_actor("Эндрю Ховард", "Геннадий")

# Показываем обновленную информацию о фильме
view.show_information()
