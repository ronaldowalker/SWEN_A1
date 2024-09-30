Ronaldo Walker
816036438
COMP3616 A1

Description
In this assignment, students shall interpret system requirements to model a solution and implement a command line application.

Project Selection

Competitions Platform
An application for students to showcase their participation in coding competitions.


Create Competition

Import competition results from file

View competitions list

View competition results

This is a documentation of all the CLI commands used 


cli = AppGroup('competitions')

This command Creates competition in the database

@cli.command('create', help="Creates competition in the database")
def create():
    create_competition()

This command List competitions in the database

@cli.command('list', help="List competitions in the database")
def list_competitions():
    view_competitions()

This command List competition results in the database

@cli.command('results', help="List competition results in the database")
def results():
    comp_id = input("Enter competition ID: ")
    view_competition_results(comp_id)


This command Imports a csv file to populate the results database

@cli.command('import', help="Imports a csv file to populate the results database")
def import_results():
    comp_id = input("Enter competition ID: ")
    file_path = input("Enter path to the results file (CSV): ")
    import_results_from_file(comp_id, file_path)
