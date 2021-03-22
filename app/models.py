from . import db
class Property(db.Model):
    __tablename__ = "properties"
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    rooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    property_type = db.Column(db.String(1000))
    location = db.Column(db.String(1000))
    photo = db.Column(db.String(30))

    def __init__(self, title, description, rooms, bathrooms,price, property_type, location, photo):
        self.title=title
        self.description=description
        self.rooms=rooms
        self.bathrooms=bathrooms
        self.price=price
        self.property_type=property_type
        self.location=location
        self.photo=photo