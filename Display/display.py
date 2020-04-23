from AjoutsFilm.Presenter.PresenterDisplay import Presenter

class display() :

	def __init__(self) : 
		# self.continuer = "o"
		# self.ListeNom = []
		self.Nom = ""

	def DemandeUser(self) : 
		   self.user = raw_input("Rentre ton user")

	def Continuer(self) : 
		self.continuer = raw_input("Continuer?")

	def giveUser (self) : 
		return self.ListeNom


	def DemanderFilm(): 
		raw_input("Rentre ton Film")

	def RentreTanote():
		pass