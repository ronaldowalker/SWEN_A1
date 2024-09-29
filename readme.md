Ronaldo Walker
816036438
COMP3616 A1

This is a documentation of all the CLI commands used 


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

@cli.command('import', help="Imports a csv file to populate the results database")
def import_results():
    comp_id = input("Enter competition ID: ")
    file_path = input("Enter path to the results file (CSV): ")
    import_results_from_file(comp_id, file_path)
