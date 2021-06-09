from flask import request
from Tests.base_test import BaseTest

class TestHomePage(BaseTest):
    def test_home(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/home', follow_redirects=True)

                self.assertEqual('http://localhost/home', request.url)
                self.assertEqual(response.status_code, 405)
