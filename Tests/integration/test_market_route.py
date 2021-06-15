from flask import request
from Tests.base_test import BaseTest
from market import db
from market.models import User, Item


class TestMarketRoute(BaseTest):
    def test_market_route(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="Poli", email_address="poli@gmail.com",
                                                   password1="12345ab", password2="12345ab",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="poli@gmail.com").first()
                self.assertIsNone(user)

                respons = self.app.post('/login', data=dict(username="Poli", password="12345ab"), follow_redirects=True)

                self.assertIn(b'Success! You are logged in as: Poli', respons.data)


                self.assertEqual('http://localhost/market', request.url)

                purchased_item = Item(id=1, name="New Product", price= 1200, barcode=7654321, description="This is a jacket", owner=1).buy(user).get_data()

                self.assertFalse(purchased_item)

                purchase_item = self.app.post('/market', follow_redirects=True).get_data()

                self.assertTrue(purchase_item)
                self.assertIn(b'Congratulations! You purchased', purchased_item)
