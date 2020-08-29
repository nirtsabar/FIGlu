import click
from flask import current_app
from flask.cli import with_appcontext

import auth


def init_app(app):
    app.teardown_appcontext(auth.close_db)
    app.cli.add_command(init_db_command)


def init_db():
    db = auth.get_db()
    print("got db")
    # schema.sql contains DROP (delete) commands
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')  # To run, in the Terminal, use the command: 'flask init-db'
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
