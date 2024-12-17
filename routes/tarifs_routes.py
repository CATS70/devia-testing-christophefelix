from flask import Blueprint, request, jsonify
from models.database import db
from models.tarifs import Tarifs

tarifs_routes = Blueprint("tarifs_routes", __name__)

@tarifs_routes.route("/tarifs", methods=["GET"])
def get_tarifs():
    tarifs = Tarifs.query.all()
    return jsonify([tarif.to_dict() for tarif in tarifs]), 200

@tarifs_routes.route("/tarifs/<int:tarif_id>", methods=["GET"])
def get_tarif(tarif_id):
    tarif = Tarifs.query.get(tarif_id)
    if tarif:
        return jsonify(tarif.to_dict()), 200
    return jsonify({"error": "Tarif not found"}), 404

@tarifs_routes.route("/tarifs", methods=["POST"])
def create_tarif():
    data = request.get_json()
    if not data.get("name") or not data.get("id")  or not data.get("tarif"):
        return jsonify({"error": "Id, name and tarif are required"}), 400

    if Tarifs.query.filter_by(id=data["id"]).first():
        return jsonify({"error": "id already exists"}), 400

    new_tarif = Tarifs(name=data["name"], id=data["id"], description=data["tarif"])
    db.session.add(new_tarif)
    db.session.commit()
    return jsonify(new_tarif.to_dict()), 201

@tarifs_routes.route("/tarifs/<int:tarif_id>", methods=["PUT"])
def update_tarif(Tarif_id):
    tarif = Tarifs.query.get(Tarif_id)
    if not tarif:
        return jsonify({"error": "id  Tarif not found"}), 404

    data = request.get_json()
    tarif.name = data.get("name", tarif.name)
    tarif.id = data.get("id", tarif.id)
    tarif.description = data.get("description", tarif.description)
    db.session.commit()
    return jsonify(tarif.to_dict()), 200

@tarifs_routes.route("/users/<int:tarif_id>", methods=["DELETE"])
def delete_user(tarif_id):
    tarif = Tarifs.query.get(tarif_id)
    if not tarif:
        return jsonify({"error": "Tarif not found"}), 404

    db.session.delete(tarif)
    db.session.commit()
    return jsonify({"message": "Tarif deleted successfully"}), 200
