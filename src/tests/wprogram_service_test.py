import unittest
from services.wprogram_service import WprogramService
from repositories.user_repository import UserRepository
from entities.user import User
from services.user_service import user_service


class TestWodService(unittest.TestCase):
    def setUp(self):
        self._ur = UserRepository()
        self._user = User("Simo", "simo1", 1)
        user_service.login("Simo", "simo1")
        self._wps = WprogramService()

    def test_initialize_wp_view(self):
        answer = self._wps.initialize_wp_view()

        self.assertEqual(answer[0].wod_id(), 1)
