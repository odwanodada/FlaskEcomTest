from flask import request
from Tests.base_test import BaseTest
from market import db
from market.models import User


class TestLogout(BaseTest):
    def test_user_logged_out_successfully(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="Odwa", email_address="odwa@gmail.com",
                                                   password1="2021069", password2="2021069",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="odwa@gmail.com").first()
                self.assertTrue(user)

                respons = self.app.post('/login', data=dict(username="Odwa", password="2021069"), follow_redirects=True)

                self.assertIn(b'Success! You are logged in as: JoeDoe', respons.data)
                self.assertEqual('http://localhost/market', request.url)
                response = self.app.post('/logout', follow_redirects=True)
                self.assertEqual('http://localhost/logout', request.url)
