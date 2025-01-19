from utils.config import db
from models.user import User

class SongRequest(db.Model):
    __tablename__ = 'song_requests'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    title=db.Column(db.String, nullable=False)
    #professional_id=
    users=db.relationship("User",back_populates="song_requests")

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title
        }