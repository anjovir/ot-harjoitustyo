class User:
    def __init__(self, username, password, user_id=""):
        self._username = username
        self._password = password
        self._id = user_id

    def username(self):
        return self._username

    def password(self):
        return self._password

    def user_id(self):
        return self._id

    def update_user_id(self, user_id):
        self._id = user_id

    # def wprogram_id(self):
    #    return self.wprogram_id

    def __str__(self):
        return f"username: {self._username}, password: {self._password}, user_id: {self._id}"
