from unittest import TestCase
from market.models import User,Item


class TestModels(TestCase):
    def test_create_user(self):
        user = User(id=1, username="Nodada", email_address="nodada@gmail.com", password_hash="dadedido")

        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, "Nodada")
        self.assertEqual(user.email_address, "nodada@gmail.com")
        self.assertEqual(user.password_hash, "dadedido")

    def test_item(self):
        item = Item(id=1, name="Iphone", price= 10000,description="IphoneX", owner=123)

        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, "Iphone")
        self.assertEqual(item.price, 10000)
        self.assertEqual(item.description, "IphoneX")
        self.assertEqual(item.owner, 123)


    def test_can_buy(self):

        item = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket", owner=1)

        user = User(id=1, username="odwa", email_address="odwa@gmail.com", password_hash="abcd", budget=5000).can_purchase(item)

        self.assertTrue(user)

    def test_can_sell_item(self):
        items = Item(id=1, name="New Product", price=200, barcode=1234567, description="This is a jacket", owner=1)

        user = User(id=1, username="odwa", email_address="odwa@gmail.com", password_hash="abcd", budget=900,).can_sell(item_obj=Item)

        self.assertFalse(user)

    def test_budget_prettier(self):

        user = User(id=1, username="odwa", email_address="odwa@gmail.com", password_hash="abcd", budget=5000)

        self.assertTrue(user.prettier_budget, 5000)





















