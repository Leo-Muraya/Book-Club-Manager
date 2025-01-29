from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from models import db, Discussion

discussions_bp = Blueprint('discussions', __name__)

@discussions_bp.route('/bookclubs/<int:club_id>/discussions', methods=['POST'])
@jwt_required()
def start_discussion(club_id):
    user_id = get_jwt_identity()
    data = request.json
    new_discussion = Discussion(book_club_id=club_id, topic=data['topic'], content=data['content'], created_by_user_id=user_id, timestamp=datetime.utcnow())
    db.session.add(new_discussion)
    db.session.commit()
    return jsonify(message='Discussion started successfully'), 201

@discussions_bp.route('/bookclubs/<int:club_id>/discussions', methods=['GET'])
@jwt_required()
def get_discussions(club_id):
    discussions = Discussion.query.filter_by(book_club_id=club_id).all()
    return jsonify([{'id': disc.id, 'topic': disc.topic, 'content': disc.content, 'timestamp': disc.timestamp} for disc in discussions]), 200
