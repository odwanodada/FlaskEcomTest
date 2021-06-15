from flask import request
from Tests.base_test import BaseTest, db
from market import db
from market.models import User


class TestLogout(BaseTest):
    def test_user_logged_out_successfully(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="Odwa", email_address="odwa@gmail.com",
                                                   password1="8-2fermENt2020", password2="8-2fermENt2020",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="odwa@gmail.com").first()
                self.assertIsNone(user)

                respons = self.app.post('/login', data=dict(username="Odwa", password="8-2fermENt2020"), follow_redirects=True)

                self.assertIn(b'Success! You are logged in as: Odwa', respons.data)
                self.assertEqual('http://localhost/market', request.url)
                response = self.app.post('/logout', follow_redirects=True)
                self.assertEqual('http://localhost/logout', request.url)
