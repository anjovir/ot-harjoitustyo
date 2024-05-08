import unittest
from initialize_database import initialize_test_database
from services.wprogram_service import WprogramService
from repositories.user_repository import UserRepository
from services.user_service import user_service

class TestWodService(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self._us = UserRepository()
        user_service.login("Pekka", "pekka1")
        self._wps = WprogramService()

    def test_initialize_wp_view(self):
        answer = self._wps.initialize_wp_view()

        self.assertEqual(answer[0].wod_id(), 1)