import json 

class EcrireJson ():
	
	structure_json = r'/Users/samirotmani/Desktop/Test Ajout Film\structure.json'
	structure_json = structure_json.replace('\\', '/')

	baseJson =  r'/Users/samirotmani/Desktop/Test Ajout Film\sBaseNoms.json'
	baseJson = baseJson.replace('\\', '/')

	def creeJsonNom(self, userlist) :
		fichier_json = '{0}/{1}-{2}'.format(self.baseJson,userlist)
		if os.path.isfile(fichier_json) : 
			print("ton fichier existe est deja present et c'est le suivant")
		else :
			with open(fichier_json,"r+") as a: 
			    data = json.load(a) 
			    data.update(userlist)   
			    a.seek(0)
			    json.dump(data, a)

			print('Creation du fichier Json {0}'.format(dossier))


s