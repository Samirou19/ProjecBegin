import Mod.dataBase.JsonUser as Json
import Mod.Entities.ListMovie as Movie
import Mod.dataBase.JsonMovie as JsonMovie
import Mod.Entities.User as User


class Presenter:
    def __init__(self, view):
        self.userUi = view
        self.userDb = Json.JsonUser()
        self.user = User.User()
        self.list_movie = Movie.ListMovie()
        self.json_movie = JsonMovie.JsonMovie()

    def save_user(self, username):
        if self.user.is_user_exist(username):
            self.userUi.user_already_exist()

        else:
            self.userDb.create_new_json()
            self.userDb.update_file_json(username)
            self.userUi.enter_movie()

    def enter_movie(self):
        self.userUi.enter_movie()

    def initialize(self):
        self.userUi.enter_user()

    def get_list_movie(self, username):
        self.json_movie.read_list_movie()
        get_list_movie = self.json_movie.return_list_movie()
        for key, values in get_list_movie[username].items():
            print("ton titre de film est {0}".format(key))
            print("sa note est {0}".format(values))

    def save_movie(self, film, note, user):
        self.list_movie.insert_movie(film, note)
        list_movie = self.list_movie.get_list_movie()
        self.list_movie.insert_user_movie(user)
        self.json_movie.update_movie_json(list_movie)
        print("enregistrement film effectue")
