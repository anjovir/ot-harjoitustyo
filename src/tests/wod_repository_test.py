import unittest
from repositories.wod_repository import WodRepository
from database_connection import connection
from repositories.user_repository import UserRepository
from entities.user import User


class TestWodRepository(unittest.TestCase):
    def setUp(self):
        self._ur = UserRepository()
        self._user = User("Simo", "simo1", 1)

        self._wr = WodRepository()
        self._wod_name = "Testitreeni"
        self._wprogram_id = 1
        self._exercise = "Testipenkki"
        self._sets = 3
        self._reps = 10
        self._weights = 70
        self._c = self._wr._connection.cursor()
        self._exercise_id = 1
        self._entry = ["Testitreeni", "Testipenkki", "3", "10", "70"]

    def test_write_method(self):
        self._wr.write([self._entry], self._wprogram_id)
        self._c.execute("SELECT * FROM wod_exercises")

        answer = self._c.fetchall()[0]
        self.assertEqual(answer[2], self._exercise)

    def test_return_last_exercise_id(self):
        self._wr.write([self._entry], self._wprogram_id)
        answer = self._wr.return_last_exercise_id()
        self.assertEqual(answer[0], self._exercise_id)
