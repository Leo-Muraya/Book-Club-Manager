from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import db, BookClub

book_clubs_bp = Blueprint('book_clubs', __name__)

@book_clubs_bp.route('/bookclubs', methods=['POST'])
@jwt_required()
def create_book_club():
    user_id = get_jwt_identity()
    data = request.json
    new_club = BookClub(name=data['name'], description=data['description'], created_by_user_id=user_id)
    db.session.add(new_club)
    db.session.commit()
    return jsonify(message='Book Club created successfully'), 201

@book_clubs_bp.route('/bookclubs', methods=['GET'])
@jwt_required()
def get_book_clubs():
    book_clubs = BookClub.query.all()
    return jsonify([{'id': club.id, 'name': club.name, 'description': club.description} for club in book_clubs]), 200

@book_clubs_bp.route('/bookclubs/<int:club_id>', methods=['DELETE'])
@jwt_required()
def delete_book_club(club_id):
    book_club = BookClub.query.get(club_id)
    if book_club:
        db.session.delete(book_club)
        db.session.commit()
        return jsonify(message='Book Club deleted successfully'), 200
    return jsonify(message='Book Club not found'), 404
