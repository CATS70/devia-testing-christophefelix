import unittest
from app import create_app
from models.database import db
from models.produits import Produits

class ProduitsTestCase(unittest.TestCase):
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

    def test_create_produits(self):
        response = self.client.post("/api/produits", json={"name": "Produit 1", "description": "desc prod 1", "id":"1"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Produit 1", str(response.data))

    def test_get_produits(self):
        self.client.post("/api/produits", json={"name": "Produit 1", "description": "desc prod 1", "id":"1"})
        response = self.client.get("/api/produits")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Produit 1", str(response.data))

    def test_get_produit(self):
        self.client.post("/api/produits", json={"name": "Produit 1", "description": "desc prod 1", "id":"1"})
        response = self.client.get("/api/produits/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Produit 1", str(response.data))

    def test_update_produit(self):
        self.client.post("/api/produits", json={"name": "Produit 1", "description": "desc prod 1", "id":"1"})
        response = self.client.put("/api/produits/1", json={"name": "Product 1"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Product 1", str(response.data))

    def test_delete_produits(self):
        self.client.post("/api/produits", json={"name": "Produit 1", "description": "desc prod 1", "id":"1"})
        response = self.client.delete("/api/produits/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Produit deleted successfully", str(response.data))

if __name__ == "__main__":
    unittest.main()
