import unittest
from entities.wod import Wod

class TestWod(unittest.TestCase):
    def setUp(self):
        self._wod = Wod()

    def test_constructor_returns_the_right_default_name(self):
        answer = self._wod.return_args()[0]
        
        self.assertEqual(answer, "Default")
    

