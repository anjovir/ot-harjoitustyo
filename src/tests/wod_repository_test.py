import unittest
from repositories.wod_repository import WodRepository
from initialize_database import initialize_test_database


class TestWodRepository(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self._wr = WodRepository()
        self._wod_name = "Testitreeni"
        self._wprogram_id = 1
        self._exercise = "Testipenkki"
        self._sets = 3
        self._reps = 10
        self._weights = 70
        self._c = self._wr._connection.cursor()
        self._exercise_id = 1

    def test_write_method(self):
        self._wr.write(self._wod_name, self._wprogram_id,
                       self._exercise, self._sets, self._reps, self._weights)
        self._c.execute("SELECT * FROM wod_exercises")

        answer = self._c.fetchall()[0]
        self.assertEqual(answer[2], self._exercise)

    def test_return_last_exercise_id(self):
        answer = self._wr.return_last_exercise_id()

        self.assertEqual(answer[0], self._exercise_id)

    def test_edit_wod(self):
        pass
