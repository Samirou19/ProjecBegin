class listMovie():
    listeUser = {}

    def __init__(self, titreDefilm='Default', Note=1):
        self.titreDefilm = titreDefilm
        self.Note = Note

    def InserFilm(self, film):
        self.ListeFilm = {}
        self.ListeFilm[film.titreDefilm] = film.Note
        print(self.ListeFilm)

    def SaveFilm(self, film, user):
        self.listeUser[user.name] = self.ListeFilm
        print(self.listeUser)
