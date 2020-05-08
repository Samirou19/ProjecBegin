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

    def enter_movie(self):
        film = input("Enter your movie")
        note = input("Enter your note")
        self.displayPresenter.construct_list_movie(film, note, self.username)

    def modify_movie(self):
        film = input("(modification)add your movie")
        note = input("(modification)Enter your note")
        self.displayPresenter.modify_user(film, note, self.username)

    def question_add_movie(self):
        response = input("Add a movie y/n")
        self.displayPresenter.continued_movie(response)

    def add_user(self):
        response = input("Add a user y/n")
        self.displayPresenter.continued_user(response)

    def question_modification(self):
        response = input("You want to modify y/n")
        self.displayPresenter.modification(response)

    @staticmethod
    def thanks():
        print("Thanks for playing")

    def return_user(self):
        return self.username
