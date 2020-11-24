import os
import csv
import psycopg2
import psycopg2.extras
import bcrypt
from . import auth

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """Get a PostgreSQL database connection object."""

    # This function returns a connection, but you will also need to open a
    # cursor for the given transaction. For SELECT queries, it would look like:
    #
    # cur = get_db().cursor()
    # cur.execute("SELECT ...")
    # result = cur.fetchone()
    # cur.close()

    if "db" not in g:
        # if there is not already a connection, open one using app
        # configuration and save it to global `g` object
        g.db = psycopg2.connect(
            current_app.config['DB_URL'],
            sslmode=current_app.config['DB_SSLMODE'],
            cursor_factory=psycopg2.extras.DictCursor
        )

    return g.db


def close_db(e=None):
    """Close the current PostgreSQL connection"""

    # remove connection object from global `g` object, if it exists
    db = g.pop("db", None)

    if db is not None:
        # close the connection
        db.close()


def init_db():
    """Clear any existing data and create all tables."""

    # open the schema file and close it when done
    with current_app.open_resource("schema.sql") as f:
        # get the database connection, save and close when done
        with get_db() as con:
            # begin a transaction
            with con.cursor() as cur:
                # use the file's text to execute the SQL queries within
                cur.execute(f.read())


@click.command("init-db")
@with_appcontext
def init_db_command():
    """CLI command to clear any existing data and create all tables."""
    init_db()
    click.echo("Initialized the database.")


def mock_db():
    """Seed the database with mock data."""

    data_filepath = os.path.join(os.path.dirname(
        __file__), os.pardir, "tests", "data.sql")
    # open the mock data file and close when done
    with open(data_filepath, "rb") as f:
        with get_db() as con:
            with con.cursor() as cur:
                cur.execute(f.read())


@click.command("mock-db")
@with_appcontext
def mock_db_command():
    """CLI command to seed the database with mock data."""
    mock_db()
    click.echo("Inserted mock data.")


def init_app(app):
    """Register database functions with app."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(mock_db_command)
    app.cli.add_command(import_csv_command)


def import_csv():
    """Seed the database with user data."""

    data_filepath = os.path.join(os.path.dirname(
        __file__), os.pardir, "import_data", "portal_users.csv")
    # open the mock data file and close when done
    with open(data_filepath, "r") as f:
        with get_db() as con:
            with con.cursor() as cur:
                reader = csv.reader(f)
                next(reader)  # Skip the header row.
                for row in reader:
                    cur.execute("""
                        INSERT INTO users (id, email, password, first_name, last_name, dob, last_login, total_login, role)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """,
                                row
                                )
                    g.db.commit()

                cur.execute(
                    "SELECT id, password FROM users"
                )
                passwords = cur.fetchall()

                for password in passwords:

                    hashed = auth.hash_pass(password[1].tobytes())

                    cur.execute(
                        'UPDATE users SET password = %s WHERE id = %s',
                        (hashed, password[0]))

                    g.db.commit()

                cur.close()


@click.command("import-csv")
@with_appcontext
def import_csv_command():
    """CLI command to seed the database with user data."""
    import_csv()
    click.echo("Inserted csv data.")
