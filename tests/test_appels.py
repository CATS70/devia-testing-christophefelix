import unittest
from app import create_app
from models.database import db
from models.appels import Appels

class AppelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_existence_data(self):
        data = Appels(email = "felix@yo.fr",message = "mon appel en clair")

        self.assertEqual(data.email,"felix@yo.fr")
        self.assertEqual(data.message,"mon appel en clair")

if __name__ == "__main__":
    unittest.main()