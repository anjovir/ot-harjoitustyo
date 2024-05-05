import unittest
from repositories.user_repository import UserRepository
from initialize_database import initialize_test_database
from entities.user import User


class TestUseRepository(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self._ur = UserRepository()
        self._user = User("Simo", "simo1", 2)

    def test_create_user(self):
        answer = self._ur.create(self._user)

        self.assertEqual(answer, self._user)
