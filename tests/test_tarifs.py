import unittest
from app import create_app
from models.database import db
from models.produits import Produits

class TarifsTestCase(unittest.TestCase):
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

    def test_create_tarifs(self):
        response = self.client.post("/api/tarifs", json={"name": "tarif 1", "tarif": 1.11, "id":"1"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("tarif 1", str(response.data))

    def test_get_tarifs(self):
        self.client.post("/api/produits", json={"name": "tarif 1", "tarif": 1.11, "id":"1"})
        response = self.client.get("/api/tarifs")
        self.assertEqual(response.status_code, 200)
        self.assertIn("tarif 1", str(response.data))

    def test_get_tarif(self):
        self.client.post("/api/produits", json={"name": "tarif 1", "tarif": 1.11, "id":"1"})
        response = self.client.get("/api/tarifs/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("tarif 1", str(response.data))

    def test_update_tarif(self):
        self.client.post("/api/produits", json={"name": "tarif 1", "tarif": 1.11, "id":"1"})
        response = self.client.put("/api/tarifs/1", json={"name": "Tarif 1"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Tarif 1", str(response.data))

    def test_delete_tarifs(self):
        self.client.post("/api/produits", json={"name": "tarif 1", "tarif": 1.11, "id":"1"})
        response = self.client.delete("/api/tarifs/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Tarif deleted successfully", str(response.data))

if __name__ == "__main__":
    unittest.main()
