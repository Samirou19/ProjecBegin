import json
import os


class JsonMovie:
    movie_json = r'/Users/samirotmani/Documents/Samir Otmani/R&d/Python/Projets/AjoutsFilm/Mod/dataBase/MovieFile.json'
    movie_json = movie_json.replace('\\', '/')
    list_movie = {}

    def create_new_json(self):
        file_json = self.movie_json
        if not os.path.isfile(file_json):
            with open(file_json, 'a') as j:
                json.dump({}, j)

    def update_movie_json(self, list_movie):
        file_json = self.movie_json
        with open(file_json, 'r+') as a:
            data = json.load(a)
            data.update(list_movie)
            a.seek(0)
            json.dump(data, a)

    def read_list_movie(self):
        file_json = self.movie_json
        with open(file_json, 'r+') as p:
            self.list_movie = json.load(p)

    def modification_movie_json(self, list_movie):
        file_json = self.movie_json
        with open(file_json, 'w') as d:
            json.dump(list_movie, d)

    def return_list_movie(self):
        return self.list_movie
