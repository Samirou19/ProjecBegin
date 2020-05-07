class ListMovie:

    def __init__(self, title_movie='Default', note=1):
        self.list_movie = {}
        self.list_user = {}
        self.title_movie = title_movie
        self.note = note

    def insert_movie(self, film, note):
        self.list_movie[film] = note

    def insert_user_movie(self, user):
        self.list_user[user] = self.list_movie

    def get_list_movie(self):
        return self.list_user

    def get_return_movie(self):
        return self.list_movie
