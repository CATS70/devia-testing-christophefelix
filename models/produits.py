from models.database import db

class Produits(db.Model):
    __tablename__ = "produits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.email}
