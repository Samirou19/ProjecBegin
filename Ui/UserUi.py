from Presenters.DisplayPresenter import DisplayPresenter


class UserUi:
    def __init__(self):
        self.displayPresenter = DisplayPresenter(self)

    def enterUser(self):
        userName = raw_input("Rentre ton user")
        self.displayPresenter.saveUser(userName)

    def userAlreadyExist(self):
        raw_input("L'utilisateur existe deja")
        self.enterMovie()

    def enterMovie(self):
        raw_input("Rentre ton Film")





    def returnUser(self):
        return self.userName
