import sys
import os

# Add the server directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.app import create_app
from server.app.models import db, User, BookClub, Book, Discussion
from werkzeug.security import generate_password_hash
from faker import Faker

# Initialize Flask app
app = create_app()

# Initialize Faker
fake = Faker()

# Push the app context
with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Create Users with fake data
    users = []
    for _ in range(10):  # Create 10 fake users
        user = User(
            name=fake.name(),
            email=fake.email(),
            password=generate_password_hash(fake.password())
        )
        users.append(user)

    # Create Book Clubs with fake data
    clubs = []
    for _ in range(5):  # Create 5 fake book clubs
        club = BookClub(
            name=fake.catch_phrase(),
            description=fake.text(max_nb_chars=200)
        )
        clubs.append(club)

    # Add Users and Book Clubs to the database and commit to generate IDs
    db.session.add_all(users + clubs)
    db.session.commit()

    # Create Books with fake data and assign to random clubs
    books = []
    for club in clubs:
        for _ in range(3):  # Create 3 books per club
            book = Book(
                title=fake.catch_phrase(),
                author=fake.name(),
                club_id=club.id
            )
            books.append(book)

    # Create Discussions with fake data and assign to random clubs
    discussions = []
    for club in clubs:
        for _ in range(2):  # Create 2 discussions per club
            discussion = Discussion(
                title=fake.sentence(),
                club_id=club.id
            )
            discussions.append(discussion)

    # Add Books and Discussions to the database
    db.session.add_all(books + discussions)
    db.session.commit()

    print("📚 Database successfully seeded with fake data!")