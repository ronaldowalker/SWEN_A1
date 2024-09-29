import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )
from App.controllers import (create_competition, view_competitions, view_competition_results, import_results_from_file)


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''



#Assignment CLI commands
cli = AppGroup('competitions')

@cli.command('create', help="Creates competition in the database")
def create():
    create_competition()

@cli.command('list', help="List competitions in the database")
def list_competitions():
    view_competitions()

@cli.command('results', help="List competition results in the database")
def results():
    comp_id = input("Enter competition ID: ")
    view_competition_results(comp_id)

@cli.command('import', help="Import csv file to populate database")
def import_results():
    comp_id = input("Enter competition ID: ")
    file_path = input("Enter path to the results file (CSV): ")
    import_results_from_file(comp_id, file_path)

app.cli.add_command(cli)