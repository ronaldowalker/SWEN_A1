from App.database import db

class result(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competitions.id'), nullable=False)
    student_name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Float, nullable=False)