from repositories.user_repository import UserRepository
from entities.user import User


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class UserService:

    def __init__(self):
        self._user_repository = UserRepository()

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def get_current_user(self):
        return self._user

    def get_users(self):
        return self._user_repository.find_all()

    def logout(self):
        self._user = None

    def create_user(self, username, password, wprogram_id, login=True):

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user


user_service = UserService()
