class UserUi:
    def __init__(self):
        self.user = ""

    def enterUser(self):
        raw_input("Rentre ton user")

    def returnUser(self):
        return self.user

    def enterMovie(self):
        self.film = raw_input("Rentre ton Film")
