from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import db, Membership

memberships_bp = Blueprint('memberships', __name__)

@memberships_bp.route('/bookclubs/<int:club_id>/join', methods=['POST'])
@jwt_required()
def join_book_club(club_id):
    user_id = get_jwt_identity()
    membership = Membership.query.filter_by(user_id=user_id, book_club_id=club_id).first()
    if membership:
        return jsonify(message='Already a member'), 400
    new_membership = Membership(user_id=user_id, book_club_id=club_id, role='Member')
    db.session.add(new_membership)
    db.session.commit()
    return jsonify(message='Joined book club'), 201

@memberships_bp.route('/bookclubs/<int:club_id>/leave', methods=['POST'])
@jwt_required()
def leave_book_club(club_id):
    user_id = get_jwt_identity()
    membership = Membership.query.filter_by(user_id=user_id, book_club_id=club_id).first()
    if membership:
        db.session.delete(membership)
        db.session.commit()
        return jsonify(message='Left book club'), 200
    return jsonify(message='Not a member of this club'), 400
