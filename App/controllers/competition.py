from flask import request, jsonify
from models import db, competition

def create_competition():
    name = input("Enter the competition name: ")
    description = input("Enter description: ")
    
    # Create and save the new competition
    competition = competition(name=name, description=description)
    db.session.add(competition)
    db.session.commit()

    print(f"Competition '{name}' created successfully.")

def view_competitions():
    competitions = competition.query.all()

    for comp in competitions:
        print(f"ID: {comp.id}, Name: {comp.name}, Description: {comp.description}")

def view_competition_results(competition_id):
    competition = competition.query.get(competition_id)
    if not competition:
        print("Competition not found.")
        return

    print(f"Results for competition: {competition.name}")
    for result in competition.results:
        print(f"Participant: {result.participant_name}, Score: {result.score}")