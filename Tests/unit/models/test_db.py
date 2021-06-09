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





















