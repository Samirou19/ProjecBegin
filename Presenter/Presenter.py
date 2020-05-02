import Mod.Entities.CreateJson as Json
import Mod.Entities.ListMovie as Movie
import Mod.Entities.CreateJsonMovie as JsonMovie


class Presenter:
    def __init__(self, view):
        self.userUi = view
        self.userDb = Json.CreateJson()
        self.list_movie = Movie.listMovie()
        self.json_movie = JsonMovie.CreateJsonMovie()

    def saveuser(self, username):
        if self.userDb.isuserexist(username):
            self.userUi.userAlreadyExist()

        else:
            self.userDb.createnewjson()
            self.userDb.updatefichierjson(username)
            self.userUi.enterMovie()

    def entermovie(self):
        self.userUi.enterMovie()

    def initialize(self):
        self.userUi.enterUser()

    def getlistemovie(self, username):
        self.json_movie.readlistmovie()
        getlistmovie = self.json_movie.returnlistemovie()
        for key, values in getlistmovie[username].items():
            print("ton titre de film est {0}".format(key))
            print("sa note est {0}".format(values))

    def savefilm(self, film, note, user):
        self.list_movie.inserFilm(film, note)
        list_movie = self.list_movie.getlistemovie()
        self.list_movie.inseruserfilm(user)
        self.json_movie.updatemoviejson(list_movie)
        print("enregistrement film effectue")

# class presenter():
#
#     def __init__(self):
#         self.nom = ""
#         self.Nom = Aff.Affichage()
#         self.Nom.DemandeUser()
#         self.nom = self.Nom.giveUser()
#         print(self.nom)
#         JsonPerso = Json.JsonPerso()
#         JsonPerso.CreerFichierJson()
#         JsonPerso.LireJsonUser()
#         self.BaseCheck = JsonPerso.LireJsonUser()
#         if self.nom in self.BaseCheck:
#             self.valeur = True
#         else:
#             self.valeur = False
#
#     def retour(self):
#         return self.valeur
#         print(self.valeur)
#
#     def SaveUser(self):
#         self.ListeUser = {}
#         self.ListeUser[1] = self.nom
#         if self.valeur == False:
#             self.base = Json.JsonPerso()
#             print(self.base)
#             print(self.ListeUser)
#             self.base.UpdateFichierJson(self.ListeUser)
#             ("Enregistrement du user")
#         else:
#             ("Nein")
#
#     def SecondStep(self):
#         if self.valeur == False:
#             self.Nom.DemanderFilm()
#         else:
#             print("tu es deja dans la base")
