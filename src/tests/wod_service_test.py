import unittest
from services.wod_service import WodService
from repositories.user_repository import UserRepository
from entities.user import User
from services.user_service import user_service


class TestWodService(unittest.TestCase):
    def setUp(self):
        self._ur = UserRepository()
        self._user = User("Simo", "simo1", 1)
        user_service.login("Simo", "simo1")
        self._ws = WodService()
        self._content = [["Test_wod", "Test exercise", 3, 10, 50]]

    def test_save_new_wod_returns_the_right_wod_id(self):
        answer = self._ws.save_new_wod(self._content)

        self.assertEqual(answer[0], True)
