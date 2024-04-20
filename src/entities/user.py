class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def username(self):
        return self._username

    def password(self):
        return self._password

    # def wprogram_id(self):
    #    return self.wprogram_id

    def __str__(self):
        return f"username: {self._username}, password: {self._password}"
