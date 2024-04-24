class User:
    """Class that describes the user
    """
    def __init__(self, username, password, user_id=""):
        """Class constructor which creates the user

        Args:
            username (str): username
            password (str): password
            _id (str, optional): user id, Defaults to "",
                                created later in the repository.
        """

        self._username = username
        self._password = password
        self._id = user_id

    def username(self):
        """Return username

        Returns:
            username: str
        """
        return self._username

    def password(self):
        """Return password

        Returns:
            password: str
        """
        return self._password

    def user_id(self):
        """Return user_id

        Returns:
            user id: int
        """
        return self._id

    def update_user_id(self, user_id):
        """Updates user id from default to new correct id,
            which is the same as in the user repository

        Args:
            user_id: int
        """
        self._id = user_id

    def __str__(self):
        """Returns the description of class attributes 

        Returns:
            String: class attributes description
        """
        return f"username: {self._username}, password: {self._password}, user_id: {self._id}"
