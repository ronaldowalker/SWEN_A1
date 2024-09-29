import csv
from models import db, Result, Competition

def import_results_from_file(competition_id, file_path):
    competition = Competition.query.get(competition_id)
    if not competition:
        print("Competition not found.")
        return

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            student_name, score = row
            result = Result(competition_id=competition.id, student_name=student_name, score=float(score))
            db.session.add(result)
    
    db.session.commit()
    print("Results imported successfully.")