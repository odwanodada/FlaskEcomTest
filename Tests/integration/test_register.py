from flask import request
from Tests.base_test import BaseTest
from market import db
from market.models import User


class TestRegister(BaseTest):
    def test_sign_up(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="Nodada", email_address="nodada@gmail.com",
                                                   password1="1234567", password2="1234567",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="nodada@gmail.com").first()


                self.assertTrue(user)
                self.assertTrue(User)
                self.assertIn(b'Account created successfully! You are now logged in as JoeDoe', response.data)
                self.assertEqual('http://localhost/market', request.url)


    def test_password_dont_match(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="Odwa", email_address="odwa@gmail.com",
                                                   password1="246810", password2="#888", ), follow_redirects=True)


                user = db.session.query(User).filter_by(email_address="odwa@gmail.com").first()


                self.assertFalse(user)


                self.assertIn(b'There was an error with creating a user: '
                              b'[&#39;Field must be equal to password1.&#39;]', response.data)
