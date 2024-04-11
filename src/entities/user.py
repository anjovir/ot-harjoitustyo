class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def username(self):
        return self.username

    def password(self):
        return self.password
    
    #def wprogram_id(self):
    #    return self.wprogram_id
    
    def __str__(self):
        return f"username: {self.username}"
    