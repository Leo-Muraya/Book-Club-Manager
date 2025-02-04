from flask import Blueprint, request, jsonify
from server.app.models import db, Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], genre=data.get('genre'), publication_year=data.get('publication_year'), description=data.get('description'))
    db.session.add(new_book)
    db.session.commit()
    return jsonify(message='Book added successfully'), 201

@books_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre} for book in books]), 200
