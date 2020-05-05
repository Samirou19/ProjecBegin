from Presenter.Presenter import Presenter


class Display:
    username: str

    def __init__(self):
        self.displayPresenter = Presenter(self)

    def enter_user(self):
        self.username = input("Enter your user")
        self.displayPresenter.save_user(self.username)

    def user_already_exist(self):
        print("User already exist")
        self.displayPresenter.get_list_movie(self.username)
        self.displayPresenter.initialize()

    def enter_movie(self):
        film = input("Enter your movie")
        note = input("Enter your note")
        self.displayPresenter.save_movie(film, note, self.username)

    def return_user(self):
        return self.username
