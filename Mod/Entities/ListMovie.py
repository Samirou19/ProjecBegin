class listMovie():
    listeUserlisteUser = {}

    def __init__(self, titreDefilm='Default', note=1):
        self.titreDefilm = titreDefilm
        self.note = note

    def InserFilm(self, film, note):
        self.ListeFilm = {}
        self.ListeFilm[film] = note

    def SaveFilm(self, film, user):
        self.listeUser[user.name] = self.ListeFilm

    def getlistemovie(self):
       return self.ListeFilm
