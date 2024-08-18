class MovieView:
    def __init__(self, controller):
        self.controller = controller

    def show_information(self):
        information = self.controller.get_information()
        print("Информация о фильме:")
        for key, value in information.items():
            print(f"{key}: {value}")

    def add_actor(self, name, role):
        self.controller.add_actor(name, role)
        print(f"Актер {name} в роли {role} добавлен.")