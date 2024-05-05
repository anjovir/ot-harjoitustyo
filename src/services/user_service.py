from repositories.user_repository import UserRepository
from entities.user import User


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class UserService:
    """Responsible for the logic of User
    """

    def __init__(self):
        """Create UserRepository-entity,
            set the user to initial state
        """
        self._user_repository = UserRepository()
        self._user = None

    def login(self, username, password):
        """Login service

        Args:
            username (str)
            password (str)

        Raises:
            InvalidCredentialsError: exception

        Returns:
            user(User): User-object
        """
        user = self._user_repository.find_by_username(username)

        if not user or user.password() != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def get_current_user(self):
        """Returns the currently logged in user

        Returns:
            User-object
        """
        return self._user

    def logout(self):
        self._user = None

    def create_user(self, username, password, login=True):
        """Create new user

        Args:
            username (str)
            password (str)
            login (bool, optional): sets created user as current user

        Raises:
            UsernameExistsError: exception

        Returns:
            User-object
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def delete_user_data(self):
        """Service which uses repository to delete user data
        """
        self._user_repository.delete_user_data(self._user)


user_service = UserService()
