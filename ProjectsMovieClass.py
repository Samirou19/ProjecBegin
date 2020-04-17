import Mod.Entities.User as User
import Mod.DataBase.usersDataBase as UserDB
import Mod.Entities.Dossier as Dos
import Mod.Entities.JsonPerso as JsonPerso
import Mod.Entities.ListeFilm as ListeFilm
import Affichage as Aff
import PresenterDisplay as Present



Lancement = Present.FirstStep()
valeur = Lancement.retour()
print(valeur)
Lancement.SaveUser()
Lancement.SecondStep()

# user1 = User.User(name = "User 1", Id = 1)
# user2 = User.User(name = "User 2", Id = 2 )
# UserDataBase = UserDB.UserBase()
# UserDataBase.Save(user1)
# UserDataBase.Save(user2)
# ListeNom = UserDataBase.GetUser()
# print(ListeNom)

# CreationDossier = Dos.CreerDossier()
# CreationDossier.creeDoss(user1)
# CreationDossier.creeDoss(user2)
# JsonPerso = JsonPerso.JsonPerso()
# JsonPerso.UpdateFichierJson(ListeNom)
# ListeFilm1 = ListeFilm.ListeFilm(titreDefilm ='Test1', Note =  6)
# ListeFilm2 = ListeFilm.ListeFilm(titreDefilm ='Test2', Note =  69)
# ListeFilm1.InserFilm(ListeFilm1)
# ListeFilm1.SaveFilm(ListeFilm1,user1)
# ListeFilm2.InserFilm(ListeFilm2)
# ListeFilm2.SaveFilm(ListeFilm2,user2)
# JsonPerso.LireJsonUser() 
# JsonPerso.LireJsonUser()

# Lancement = Aff.Affichage()
# Lancement.DemandeUser()
# listeNom = Lancement.giveUser()
# print(listeNom)

