class Display:

    def __init__(self):
        self.Nom = ""

    def ask_user(self):
        self.user = input("Rentre ton user")

    def continued(self):
        self.continuer = input("Continuer?")

    def give_user(self):
        return self.Nom

    def put_movie(self):
        self.movie = input("Rentre ton Film")

    def insert_note(self):
        pass
