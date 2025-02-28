from models.database import db

class Appels(db.Model):
    __tablename__ = "appels"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {"id": self.id, "email": self.email, "message": self.message}