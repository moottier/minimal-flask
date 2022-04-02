from app.models import db

class Fact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submitted_by = db.Column(db.String(80), unique=True, nullable=False)
    verified = db.Column(db.String(120), db.ForeignKey('user.id'), unique=True, nullable=False)
    source = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username