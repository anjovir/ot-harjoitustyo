import unittest
from repositories.user_repository import UserRepository
from entities.user import User

class TestUseRepository(unittest.TestCase):
    def setUp(self):
        self._ur = UserRepository()
        self._user = User("Simo", "simo1", 2)

    def test_create_user(self):
        answer = self._ur.create(self._user)

        self.assertEqual(answer, self._user)
