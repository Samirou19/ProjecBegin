from Ui import Affichage as Aff
import Mod.Entities.JsonPerso as Json

class DisplayPresenter:
    def __init__(self):
        self.nom = ""
        self.Nom = Aff.Affichage()
        self.Nom.DemandeUser()
        self.nom = self.Nom.giveUser()


        print(self.nom)
        JsonPerso = Json.JsonPerso()
        JsonPerso.CreerFichierJson()
        JsonPerso.LireJsonUser()
        self.BaseCheck = JsonPerso.LireJsonUser()
        if self.nom in self.BaseCheck:
            self.valeur = True
        else:
            self.valeur = False

    def retour(self):
        print(self.valeur)
        return self.valeur

    def SaveUser(self):
        self.ListeUser = {}
        self.ListeUser[1] = self.nom
        if self.valeur == False:
            self.base = Json.JsonPerso()
            print(self.base)
            print(self.ListeUser)
            self.base.UpdateFichierJson(self.ListeUser)
            ("Enregistrement du user")
        else:
            ("Nein")

    def SecondStep(self):
        if self.valeur == False:
            self.Nom.DemanderFilm()
        else:
            print("tu es deja dans la base")
