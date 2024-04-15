import unittest
from repositories.wod_repository import WodRepository
from initialize_database import initialize_database


class TestWodRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self._wr = WodRepository()
        self._wod_name = "Testitreeni"
        self._wprogram_id = 1
        self._exercise = "Testipenkki"
        self._sets = 3
        self._reps = 10
        self._weights = 70
        self._c = self._wr._connection.cursor()
        

    def test_constructor_returns_the_right_default_name(self):
        pass

    def test_write_method(self):
        self._wr.write(self._wod_name, self._wprogram_id, self._exercise, self._sets, self._reps, self._weights)
        self._c.execute("SELECT * FROM wod_exercises")

        answer = self._c.fetchall()[0]
        self.assertEqual(answer[2], self._exercise)
        
        

        
