import json
import os

class UserDatabase():
    baseJson = r'/Users/hakim/Documents/Develop/Python/Samir_project/file_saved/sBaseNoms.json'
    baseJson = baseJson.replace('\\', '/')

    def isUserExist(self, name):
        userJson = self.readJsonUser()
        if name in userJson:
            return True
        return False

    def readJsonUser(self):
        fichier_json = self.baseJson
        with open(fichier_json, 'r+') as p:
            data = json.load(p)
            temp = (data)
            return temp









#TODO
    def saveUserJson(self, userName):
        fichier_json = self.baseJson
        if not os.path.isfile(fichier_json):
            print("ton fichier existe pas et nous allons le creer")
            with open(fichier_json, 'a') as j:
                json.dump({}, j)

    def UpdateFichierJson(self, userlist):
        fichier_json = self.baseJson
        with open(fichier_json, "r+") as a:
            data = json.load(a)
            data.update(userlist)
            a.seek(0)
            json.dump(userlist, a)
        print('update du fichier Json')
