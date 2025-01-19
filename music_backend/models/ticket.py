from utils.config import db


class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ticket_class = db.Column(db.String, nullable=False)  # Renamed from 'Class' to avoid conflict with Python keyword
    seat = db.Column(db.String, nullable=False)
    amount_paid = db.Column(db.Float, nullable=False)
    qr_code = db.Column(db.String, nullable=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    events = db.relationship('Event', back_populates='tickets')

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "ticket_class":self.ticket_class,
            "seat":self.seat,
            "amount_paid":self.amount_paid,
            "qr_code":self.qr_code,
            "event_id":self.event_id
            
        }


    def __repr__(self):
        return f"<Ticket (id={self.id}, name={self.name}, seat={self.seat})>"