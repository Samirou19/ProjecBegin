import json
import os


class JsonMovie:
    movie_json = r'/Users/samirotmani/Documents/Samir Otmani/R&d/Python/Projets/AjoutsFilm/Mod/dataBase/MovieFile.json'
    movie_json = movie_json.replace('\\', '/')
    list_movie = {}

    def create_new_json(self):
        file_json = self.movie_json
        if not os.path.isfile(file_json):
            print("ton fichier existe pas et nous allons le creer")
            with open(file_json, 'a') as j:
                json.dump({}, j)

    def update_movie_json(self, list_movie):
        file_json = self.movie_json
        with open(file_json, 'r+') as a:
            data = json.load(a)
            data.update(list_movie)
            a.seek(0)
            json.dump(data, a)
        print('update du fichier Json')

    def read_list_movie(self):
        file_json = self.movie_json
        with open(file_json, 'r+') as p:
            self.list_movie = json.load(p)

    def return_list_movie(self):
        return self.list_movie