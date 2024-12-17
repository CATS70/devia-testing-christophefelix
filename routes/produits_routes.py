from flask import Blueprint, request, jsonify
from models.database import db
from models.produits import Produits

produits_routes = Blueprint("produits_routes", __name__)

@produits_routes.route("/produits", methods=["GET"])
def get_produits():
    produits = Produits.query.all()
    return jsonify([prod.to_dict() for prod in produits]), 200

@produits_routes.route("/produits/<int:produit_id>", methods=["GET"])
def get_produit(produit_id):
    produit = Produits.query.get(produit_id)
    if produit:
        return jsonify(produit.to_dict()), 200
    return jsonify({"error": "Produit not found"}), 404

@produits_routes.route("/produits", methods=["POST"])
def create_produit():
    data = request.get_json()
    if not data.get("name") or not data.get("id")  or not data.get("description"):
        return jsonify({"error": "Id, name and description are required"}), 400

    if Produits.query.filter_by(id=data["id"]).first():
        return jsonify({"error": "id already exists"}), 400

    new_produit = Produits(name=data["name"], id=data["id"], description=data["description"])
    db.session.add(new_produit)
    db.session.commit()
    return jsonify(new_produit.to_dict()), 201

@produits_routes.route("/produits/<int:produit_id>", methods=["PUT"])
def update_produit(produit_id):
    produit = Produits.query.get(produit_id)
    if not produit:
        return jsonify({"error": "id  produit not found"}), 404

    data = request.get_json()
    produit.name = data.get("name", produit.name)
    produit.description = data.get("description", produit.description)
    db.session.commit()
    return jsonify(produit.to_dict()), 200

@produits_routes.route("/users/<int:produit_id>", methods=["DELETE"])
def delete_produits(produit_id):
    produit = Produits.query.get(produit_id)
    if not produit:
        return jsonify({"error": "Produit not found"}), 404

    db.session.delete(produit)
    db.session.commit()
    return jsonify({"message": "Produit deleted successfully"}), 200
