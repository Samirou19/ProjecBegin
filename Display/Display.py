from Presenter.Presenter import Presenter


class Display:
    def __init__(self):
        self.displayPresenter = Presenter(self)

    def enterUser(self):
        self.username = input("Rentre ton user")
        self.displayPresenter.saveuser(self.username)

    def userAlreadyExist(self):
        print("L'utilisateur existe deja")
        self.displayPresenter.getlistemovie()
        self.displayPresenter.initialize()

    def enterMovie(self):
        film = input("Rentre ton Film")
        note = input("rentre ta note")
        self.displayPresenter.savefilm(film, note, self.username)

    def returnUser(self):
        return self.username

# class Display:
#
#     def __init__(self):
#         self.user = ""
#         self.continued = ""
#         self.movie = ""
#
#     def ask_user(self):
#         self.user = input("Rentre ton user")
#
#     def continued(self):
#         self.continued = input("Continuer?")
#
#     def give_user(self):
#         return self.user
#
#     def put_movie(self):
#         self.movie = input("Rentre ton Film")
#
#     def insert_note(self):
#         pass
