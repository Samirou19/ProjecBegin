import Mod.Entities.UserDatabase as Json


class DisplayPresenter:
    def __init__(self, view):
        self.view = view
        self.userDb = Json.UserDatabase()

    def saveUser(self, userName):
        if self.userDb.isUserExist(userName):
            self.view.userAlreadyExist()
        else:
            self.view.enterMovie()
