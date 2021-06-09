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
                self.assertIn(b'Account created successfully! You are now logged in as', response.data)
                self.assertEqual('http://localhost/market', request.url)
