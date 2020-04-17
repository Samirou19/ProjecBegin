import json 
import os

class JsonPerso ():
	
	structure_json = r'/Users/samirotmani/Desktop/Test Ajout Film\structure.json'
	structure_json = structure_json.replace('\\', '/')

	self.baseJson =  r'/Users/samirotmani/Desktop/Test Ajout Film\sBaseNoms.json'
	self.baseJson = baseJson.replace('\\', '/')

	def creeJsonNom(self, userlist) :
		fichier_json = self.baseJson
		if not os.path.isfile(fichier_json) : 
			print("ton fichier existe pas et nous allons le creer")
			with open(fichier_json, 'a') as j :
				 json.dump({},j)
			with open(fichier_json,"r+") as a: 
			    data = json.load(a) 
			    data.update(userlist)   
			    a.seek(0)
			    json.dump(userlist, a)

			print('Creation du fichier Json')

		else :
			with open(fichier_json,"r+") as a:  
			    data = json.load(a) 
			    data.update(userlist)   
			    a.seek(0)
			    json.dump(userlist, a)

			print('Creation du fichier Json')



