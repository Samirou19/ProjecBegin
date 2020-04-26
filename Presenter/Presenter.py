import Mod.Entities.CreateJson as Json
import Mod.Entities.ListMovie as Movie
import Mod.Entities.CreateJsonMovie as JsonMovie


class Presenter:
    def __init__(self, view):
        self.userUi = view
        self.userDb = Json.CreateJson()
        self.listefilm = Movie.listMovie()
        self.jsonmovie = JsonMovie.CreateJsonMovie()

    def saveuser(self, username):
        if self.userDb.isuserexist(username):
            print("yes")
            self.userUi.userAlreadyExist()

        else:
            print("no")
            self.userDb.createnewjson()
            self.userDb.updatefichierjson(username)
            self.userUi.enterMovie()

    def savefilm(self, film, note, user):
        self.listefilm.inserFilm(film, note)
        listefilm = self.listefilm.getlistemovie()
        print(listefilm)
        self.listefilm.inseruserfilm(user)
        self.jsonmovie.updatemoviejson(listefilm)
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
