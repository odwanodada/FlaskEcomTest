from flask import request
from Tests.base_test import BaseTest
from market import db
from market.models import User


class TestRegister(BaseTest):
    def test_register_new_user(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="JoeDoe", email_address="joe@gmail.com",
                                                   password1="202177", password2="202177",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                # Asserting that the user is found in the database
                self.assertTrue(user)

                # Checking that the user has a budget of 1000
                budget = db.session.query(User).filter_by(budget=1000).first()

                # Asserting that the user has a budget of 1000
                self.assertTrue(budget)

                # asserting that the user is shown the message below
                self.assertIn(b'Account created successfully! You are now logged in as JoeDoe', response.data)

                # Asserting that the user is redirected to the market page
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



    def test_password_setter_method(self):
        with self.app:
            with self.app_context:
                # Registering a new user
                response = self.app.post('/register',
                                         data=dict(id=1, username="od", email_address="od@gmail.com",
                                                   password1="7766551", password2="7766551",), follow_redirects=True)

                user1 = db.session.query(User).filter_by(email_address="od@gmail.com").first()

                self.assertNotEqual(user1.password_hash, "7766551")



    def test_user_exists(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register', data=dict(username="God", email_address="god@gmail.com",
                                                                password1=1234567, password2=1234567), follow_redirects=True)

        
                user = db.session.query(User).filter_by(email_address="god@gmail.com").first()


                self.assertTrue(user)

                respons = self.app.post('/register', data=dict(username="God", email_address="god@gmail.com",
                                                                password1=1234567, password2=1234567), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="joe@gmail.com").first()

                self.assertTrue(user)
                self.assertIn(b'There was an error with creating a user: [&#39;Username '
                              b'already exists! Please try a different username&#39;]', respons.data)
