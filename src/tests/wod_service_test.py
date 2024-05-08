import unittest
from initialize_database import initialize_test_database
from services.wod_service import WodService
from repositories.user_repository import UserRepository
from entities.user import User
from services.user_service import user_service

class TestWodService(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self._us = UserRepository()
        user_service.login("Pekka", "pekka1")
        self._ws = WodService()
        self._content = [["Test_wod", "Test exercise", 3, 10, 50]]

    def test_save_new_wod_returns_the_right_wod_id(self):
        answer = self._ws.save_new_wod(self._content)

        self.assertEqual(answer[0], True)

