import unittest

from project.server import db
from base import BaseTestCase
from project.server.models import User


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(email='sommail@de.de', password='somepass')
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token,bytes))

    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token) == user.id)
        

if __name__== '__main__ ':
    unittest.main()