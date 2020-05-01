class listMovie():

    def __init__(self, titreDefilm='Default', note=1):
        self.ListeFilm = {}
        self.listeUser = {}
        self.titreDefilm = titreDefilm
        self.note = note

    def inserFilm(self, film, note):
        self.ListeFilm[film] = note

    def inseruserfilm(self, user):
        self.listeUser[user] = self.ListeFilm
        a = self.listeUser
        print(a)

    def getlistemovie(self):
        return self.listeUser
