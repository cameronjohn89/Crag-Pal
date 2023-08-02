from database import db


class Climb(db.Model):
    __tablename__ = 'climb'

    climb_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.user_id'), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey(
        'route.route_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    # Define relationships with other entities
    user = db.relationship('User', backref=db.backref('climb'))
    route = db.relationship('Route', backref=db.backref('climb'))

    # Add any additional attributes or methods as needed
