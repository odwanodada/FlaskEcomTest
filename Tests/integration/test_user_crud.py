from Tests.base_test import BaseTest, db
from market.models import User

class UserCrudTest(BaseTest):
    def test_user_crud(self):
        with self.app:
            with self.app_context:
                new_user = User(username='Od', email_address='odwa@gmail.com', password_hash='8-20fermENt2020', budget=500000)


                self.assertIsNone(db.session.query(User).filter_by(email_address='odwa@gmail.com').first())


                db.session.add(new_user)
                db.session.commit()
                self.assertIsNotNone(db.session.query(User).filter_by(email_address='odwa@gmail.com').first())


                db.session.delete(new_user)
                db.session.commit()
                self.assertIsNone(db.session.query(User).filter_by(email_address='odwa@gmail.com').first())
