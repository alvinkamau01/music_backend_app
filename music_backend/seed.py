from app import app
from utils.config import db
from models.user import User
from models.event import Event
from models.ticket import Ticket
from models.professional import Professional
from models.song_request import SongRequest


def seed():
    with app.app_context():
        # Drop all existing tables and create new ones
        db.drop_all()
        db.create_all()

        # Create and add users
        user1 = User(username='admin', email='admin@example.com', password='password', confirm_password="password")
        user2 = User(username='user', email='user@example.com', password='password', confirm_password="password")
        db.session.add(user1)
        db.session.add(user2)

        # Create and add events
        event1 = Event(name="Sol fest", latitude=132.3, longitude=1234.4, description="Quite a nice place", price=1332.23, date="12-12-24", banner_photo="")
        db.session.add(event1)

        # Create and add tickets
        ticket1 = Ticket(
            id=0,
            name="Ticket1",
            ticket_class="VIP",
            seat="b1",
            amount_paid="2000",  # Corrected typo from 'amoutn_paid' to 'amount_paid'
            qr_code="1832843934",
            event_id=event1.id  # Assuming you want to link the ticket to the created event
        )
        db.session.add(ticket1)

        # Create and add song requests
        song_request1 = SongRequest(title="Nitangoja", user_id=user1.id)  # Assuming you want to link the song request to user1
        db.session.add(song_request1)

        # Create and add professionals
        professional1 = Professional(song_path='path', about="about", socials="socials", banner_image="banner_image")
        db.session.add(professional1)

        # Commit all changes to the database
        db.session.commit()
        print("database seeded successfully")


if __name__ == "__main__":
    seed()