import Mod.dataBase.JsonUser as Json


class User:

    def __init__(self):
        self.file_son = Json.JsonUser()

    def is_user_exist(self, name):
        self.user_json = self.file_son.read_json_user()
        if name in self.user_json:
            return True
        return False

    def get_user(self):
        return self.file_son.read_json_user
