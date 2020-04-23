from Presenter.Presenter import Presenter


class Display:
    def __init__(self):
        self.displayPresenter = Presenter(self)

    def enterUser(self):
        userName = input("Rentre ton user")
        self.displayPresenter.saveuser(userName)

    def userAlreadyExist(self):
        input("L'utilisateur existe deja")
        self.enterMovie()

    def enterMovie(self):
        input("Rentre ton Film")

    def returnUser(self):
        return self.userName

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
