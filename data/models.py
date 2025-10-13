from data import db
from werkzeug.security import generate_password_hash, check_password_hash

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

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    _password_hash = db.Column("password", db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, plain_text_password):
        self._password_hash = generate_password_hash(plain_text_password)

    def check_password(self, plain_text_password):
        return check_password_hash(self._password_hash, plain_text_password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self._password_hash
        }


class Locations(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(50), nullable=False)
    image_mimetype = db.Column(db.String(50), nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, location_name, image_data, image_mimetype, description):
        self.location_name = location_name
        self.image_mimetype = image_mimetype
        self.image_data = image_data
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'location_name': self.location_name,
            'image_mimetype': self.image_mimetype,
            'image_data': self.image_data,
            'description': self.description,
        }
