import json
import os


class CreateJson():
    baseJson = r'/Users/samirotmani/Documents/Samir Otmani/R&d/Python/Projets/AjoutsFilm/Mod/dataBase/sBaseNoms.json'
    baseJson = baseJson.replace('\\', '/')

    def isuserexist(self, name):
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

    # TODO
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


# class createJson():
#     baseJson = r'/Users/samirotmani/Desktop/Test Ajout Film\sBaseNoms.json'
#     baseJson = baseJson.replace('\\', '/')
#
#     def CreerFichierJson(self):
#         fichier_json = self.baseJson
#         if not os.path.isfile(fichier_json):
#             print("ton fichier existe pas et nous allons le creer")
#             with open(fichier_json, 'a') as j:
#                 json.dump({}, j)
#
#     def UpdateFichierJson(self, userlist):
#         fichier_json = self.baseJson
#         with open(fichier_json, "r+") as a:
#             data = json.load(a)
#             data.update(userlist)
#             a.seek(0)
#             json.dump(userlist, a)
#         print('update du fichier Json')
#
#     def LireJsonUser(self):
#         fichier_json = self.baseJson
#         with open(fichier_json, 'r+') as p:
#             data = json.load(p)
#             temp = (data)
#             return temp
