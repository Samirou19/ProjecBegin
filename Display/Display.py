class Display:

    def __init__(self):
        self.user = ""
        self.continued = ""
        self.movie = ""

    def ask_user(self):
        self.user = input("Rentre ton user")

    def continued(self):
        self.continued = input("Continuer?")

    def give_user(self):
        return self.user

    def put_movie(self):
        self.movie = input("Rentre ton Film")

    def insert_note(self):
        pass
