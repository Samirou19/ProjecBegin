import json 
import os

class JsonPerso ():
	
	# structure_json = r'/Users/samirotmani/Desktop/Test Ajout Film\structure.json'
	# structure_json = structure_json.replace('\\', '/')

	baseJson =  r'/Users/hakim/Documents/Develop/Python/Samir_project/file_saved/sBaseNoms.json'
	baseJson = baseJson.replace('\\', '/')


	def CreerFichierJson(self) :
		fichier_json = self.baseJson
		if not os.path.isfile(fichier_json) : 
			print("ton fichier existe pas et nous allons le creer")
			with open(fichier_json, 'a') as j :
				 json.dump({},j)



	def UpdateFichierJson(self, userlist) :
		fichier_json = self.baseJson
		with open(fichier_json,"r+") as a: 
		    data = json.load(a) 
		    data.update(userlist)   
		    a.seek(0)
		    json.dump(userlist, a)
		print('update du fichier Json')

	def LireJsonUser(self) :
		fichier_json = self.baseJson
		with open(fichier_json, 'r+') as p:
 		 data = json.load(p)
 		 temp = (data)
 		 return temp
