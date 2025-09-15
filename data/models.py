from data import db
class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    special_note = db.Column(db.String(50), nullable=True)
    travel_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, email, phone, destination, travel_date, special_note):
        self.name = name
        self.email = email
        self.phone = phone
        self.destination = destination
        self.special_note = special_note
        self.travel_date = travel_date

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'tour_type': self.tour_type,
            'destination': self.destination,
            'date': self.travel_date,
            'special_note': self.special_note,
        }