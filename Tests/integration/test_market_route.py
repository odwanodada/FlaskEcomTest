from flask import request

from Tests.base_test import BaseTest
from market import db
from market.models import User, Item


class TestMarketRoute(BaseTest):
    def test_market_route_can_purchase(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(username="Langa", email_address="langa@gmail.com",
                                                   password1="1234567", password2="1234567",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="langa@gmail.com").first()
                self.assertTrue(user)

                respons = self.app.post('/login', data=dict(username="Langa", password="1234567"), follow_redirects=True)

                self.assertIn(b'Success! You are logged in as: Langa', respons.data)

                # Asserting that the user is redirected to the market page after login
                self.assertEqual('ttp://localhost/market', request.url)

                # no need for a post request because the user is redirected to the market route automatically
                market_post_request = self.app.post('/market', follow_redirects=True)
                self.assertTrue(market_post_request.status_code, 200)

                purchased_item = Item(id=1, name="New Product", price=200, barcode=7654321,
                                      description="This is a jacket")

                purchased_item1 = Item(id=1, name="New Product", price=2000, barcode=7654321,
                                       description="This is a jacket")

                self.assertTrue(user.can_purchase(purchased_item))
                self.assertFalse(user.can_purchase(purchased_item1))

    def test_market_route_can_sell(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/register',
                                         data=dict(id=1, username="Zulu", email_address="zulu@gmail.com",
                                                   password1="0246810", password2="0246810",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="zulu@gmail.com").first()
                self.assertTrue(user)


                self.assertEqual('http://localhost/market', request.url)

                purchased_item = Item(id=1, name="New Product", price=200, barcode=1234567,
                                      description="This is a jacket", owner=1)
                db.session.add(purchased_item)
                db.session.commit()

                self.assertTrue(user.can_sell(purchased_item))

    def test_market_route_returns_market(self):
        with self.app:
            with self.app_context:
                response1 = self.app.post('/register',
                                          data=dict(id=2, username="JoDoe", email_address="jo@gmail.com",
                                                    password1="202176", password2="202176",), follow_redirects=True)

                response = self.app.post('/market', follow_redirects=True)

                self.assertEqual('http://localhost/market', request.url)
