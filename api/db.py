# db.py
import mysql.connector
from flask import g
from flask.cli import with_appcontext
from api.config import Config


def get_db():
    if "db" not in g:
        g.db = mysql.connector.connect(**Config.MYSQL_CONFIG)
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    cursor = db.cursor()

    # Add database initialization queries here
    # ...

    db.commit()

    cursor.close()
