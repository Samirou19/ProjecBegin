import Mod.dataBase.JsonUser as Json
import Mod.Entities.ListMovie as Movie
import Mod.dataBase.JsonMovie as JsonMovie
import Mod.Entities.User as User


class Presenter:
    def __init__(self, view):
        self.userUi = view
        self.userDb = Json.JsonUser()
        self.user = User.User()
        self.json_movie = JsonMovie.JsonMovie()

    def save_user(self, username):
        if self.user.is_user_exist(username):
            self.userUi.user_already_exist()
            self.userUi.question_modification()

        else:
            self.list_movie = Movie.ListMovie()
            self.userDb.create_new_json()
            self.userUi.enter_movie()
            self.userDb.update_file_json(username)

    def enter_movie(self):
        self.userUi.enter_movie()

    def continued_movie(self, response):
        if response == "y":
            self.userUi.enter_movie()
        elif response == "n":
            self.userUi.add_user()
        else:
            self.userUi.enter_movie()

    def continued_user(self, response):
        if response == "y":
            self.userUi.enter_user()
        elif response == "n":
            self.userUi.thanks()
        else:
            self.userUi.add_user()

    def modification(self, response):
        if response == "y":
            self.userUi.modify_movie()
        elif response == "n":
            self.userUi.add_user()
        else:
            self.userUi.question_add_movie()

    def modification_note(self):
        pass

    def get_list_movie(self, username):
        self.json_movie.read_list_movie()
        get_list_movie = self.json_movie.return_list_movie()
        for key, values in get_list_movie[username].items():
            print("ton titre de film est {0}".format(key))
            print("sa note est {0}".format(values))

    def construct_list_movie(self, film, note, user):
        self.list_movie.insert_movie(film, note)
        self.list_movie.insert_user_movie(user)
        list_movie = self.list_movie.get_list_movie()
        self.json_movie.update_movie_json(list_movie)
        self.userUi.question_add_movie()

    def modify_user(self, film, note, user):
        list_movie = self.json_movie.return_list_movie()
        if film in list_movie[user].keys():
            self.list_movie = Movie.ListMovie()
            list_movie = self.list_movie.insert_movie(film, note)
            self.json_movie.update_movie_json(list_movie)
        self.userUi.question_modification()
