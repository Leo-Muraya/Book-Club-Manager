#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app, db
from models import User, BookClub, Book

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():        
        db.create_all()

        user1 = User(username="Alice", email="alice@example.com", password="hashedpassword")
        user2 = User(username="Bob", email="bob@example.com", password="hashedpassword")

        club1 = BookClub(name="Sci-Fi Lovers", description="A club for science fiction enthusiasts", created_by_user_id=1)
        club2 = BookClub(name="Mystery Readers", description="Solving mysteries one book at a time", created_by_user_id=2)

        book1 = Book(title="Dune", author="Frank Herbert")
        book2 = Book(title="Sherlock Holmes", author="Arthur Conan Doyle")

        db.session.add_all([user1, user2, club1, club2, book1, book2])
        db.session.commit()
