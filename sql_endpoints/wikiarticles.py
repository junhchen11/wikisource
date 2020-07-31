from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from server import app, db


@app.route('/instructors', methods=['GET'])
def select():
        try:
            # Query
            result = db.engine.execute("SELECT * FROM wikiarticles;")
            if result is None:

            return {"message": "Invalid query."}
            rows = result.fetchall()
            # Parse Output

            row_dicts = [dict(row) for row in rows]

            row_data = {"data": row_dicts}
            # return

            return row_data

        except Exception as e:

            return {"message": dict(e)}, "hello sample"


@app.route("/selectFacebook")
def selectFacebook():
    try:
        # Query
        result = db.engine.execute(
            "SELECT url FROM wikiarticles WHERE name = 'Facebook';"
        )
        if result is None:

            return {"message": "Invalid query."}
        rows = result.fetchall()
        # Parse Output

        row_dicts = [dict(row) for row in rows]

        row_data = {"data": row_dicts}
        # return

        return row_data

    except:

        return "select Failed"


@app.route("/insert")
def insert():
    try:
        # Query
        db.engine.execute(
            "INSERT INTO wikiarticles VALUES ('https://en.wikipedia.org/wiki/Facebook', 'Facebook', 9000, 'Social media')"
        )
        return "insertion successful"
    except:
        return "insertion failed"


@app.route("/delete")
def delete():
    try:
        # Query
        db.engine.execute(
            "DELETE FROM wikiarticles WHERE URL = 'https://en.wikipedia.org/wiki/Facebook'"
        )
        return "deletion successful"
    except:
        return "deletion failed"
