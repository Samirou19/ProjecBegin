import json
import os


class JsonUser:
    baseJson = r'/Users/samirotmani/Documents/Samir Otmani/R&d/Python/Projets/AjoutsFilm/Mod/dataBase/sBaseNoms.json'
    baseJson = baseJson.replace('\\', '/')

    def read_json_user(self):
        file_json = self.baseJson
        with open(file_json, 'r+') as p:
            data = json.load(p)
            return data

    def create_new_json(self):
        file_json = self.baseJson
        if not os.path.isfile(file_json):
            with open(file_json, 'a') as j:
                json.dump({}, j)

    def update_file_json(self, name):
        file_json = self.baseJson
        with open(file_json, 'r+') as a:
            data = json.load(a)
            data.update({name: "test"})
            a.seek(0)
            json.dump(data, a)
        print('update file json')
