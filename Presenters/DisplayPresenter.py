import Mod.Entities.UserDatabase as Json

class DisplayPresenter:
    def __init__(self, view):
        self.userUi = view
        self.userDb = Json.UserDatabase()

    def saveUser(self, userName):
        if self.userDb.isUserExist(userName):
            print("yes")
            self.userUi.userAlreadyExist()
        else:
            print("no")
