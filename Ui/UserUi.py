from Presenters.DisplayPresenter import DisplayPresenter


class UserUi:
    def __init__(self):
        self.displayPresenter = DisplayPresenter()

    def enterUser(self):
        userName = raw_input("Rentre ton user")
        self.displayPresenter.saveUser()

    def returnUser(self):
        return self.userName

    def enterMovie(self):
        self.film = input("Rentre ton Film")
