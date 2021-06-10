from flask import request
from Tests.base_test import BaseTest

class TestRoute(BaseTest):
    def test_home_route(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/home', follow_redirects=True)

                self.assertEqual('http://localhost/home', request.url)
                self.assertEqual(response.status_code, 200)

    def test_market_post_route(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/market', follow_redirects=True)

                self.assertEqual('http://localhost/login?next=%2Fmarket', request.url)
                self.assertEqual(response.status_code, 200)

    def test_market_get_route(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/market', follow_redirects=True)

                self.assertEqual('http://localhost/login?next=%2Fmarket', request.url)
                self.assertEqual(response.status_code, 200)

    def test_reg_get_route(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/register', follow_redirects=True)

                self.assertEqual('http://localhost/register', request.url)
                self.assertEqual(response.status_code, 200)

    def test_reg_post_route(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register', follow_redirects=True)

                self.assertEqual('http://localhost/register', request.url)
                self.assertEqual(response.status_code, 200)


    def test_login_post_route(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/login', follow_redirects=True)

                self.assertEqual('http://localhost/login', request.url)
                self.assertEqual(response.status_code, 200)

    def test_login_get_route(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/login', follow_redirects=True)

                self.assertEqual('http://localhost/login', request.url)
                self.assertEqual(response.status_code, 200)


    def test_logout_route(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/logout', follow_redirects=True)

                self.assertEqual('http://localhost/home', request.url)
                self.assertEqual(response.status_code, 200)
