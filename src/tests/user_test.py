import unittest
from entities.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self._user = User("testihenkilö", "testisalasana",1)

    def test_constructor_works(self):
        user = User("testihenkilö", "testisalasana")
        self.assertEqual(self._user.username(), user.username())
        self.assertEqual(self._user.password(), user.password())

    def test_username_method_returns_the_right_username(self):
        usernaname = self._user.username()
        self.assertEqual(usernaname, "testihenkilö")

    def test_password_method_returns_the_right_password(self):
        password = self._user.password()
        self.assertEqual(password, "testisalasana")

    def test_to_string_operator(self):
        answer = self._user.__str__()
        self.assertEqual(
            answer, "username: testihenkilö, password: testisalasana, user_id: 1")
