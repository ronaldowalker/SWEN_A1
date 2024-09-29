from App.database import db

class competition(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    
    results = db.relationship('result', backref='competition', lazy=True)