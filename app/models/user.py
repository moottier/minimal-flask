from app.models import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer)
    first_name = db.Column(db.String(120))
    facts = db.relationship('Fact', lazy='select', backref=db.backref('person', lazy='joined'))

    def __repr__(self):
        return '<User %r>' % self.username