from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import BookClub, Membership, User
from app.extensions import db

clubs_bp = Blueprint('clubs', __name__, url_prefix='/api')

@clubs_bp.route('/clubs', methods=['GET'])
def get_clubs():
    clubs = BookClub.query.all()
    return jsonify([{
        'id': club.id,
        'name': club.name,
        'description': club.description,
        'member_count': len(club.members)
    } for club in clubs]), 200

@clubs_bp.route('/clubs/<int:club_id>', methods=['GET'])
def get_club(club_id):
    club = BookClub.query.get_or_404(club_id)
    return jsonify({
        'id': club.id,
        'name': club.name,
        'description': club.description,
        'books': [{'id': b.id, 'title': b.title} for b in club.books],
        'discussions': [{'id': d.id, 'title': d.title} for d in club.discussions],
        'members': [{'id': m.user.id, 'username': m.user.username} for m in club.members]
    }), 200

@clubs_bp.route('/my-clubs', methods=['GET'])
@jwt_required()
def get_my_clubs():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify([{
        'id': membership.club.id,
        'name': membership.club.name,
        'role': membership.role
    } for membership in user.clubs]), 200