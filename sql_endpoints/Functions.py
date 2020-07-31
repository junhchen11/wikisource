from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from server import app, db


@app.route("Info")
def info():
    try:
        # Query
        result = db.engine.execute("SELECT * FROM info;")
        if result is None:
            return {"message": "Invalid query."}

        rows = result.fetchall()
        # Parse Output

        row_dicts = [dict(row) for row in rows]

        row_data = {"data": row_dicts}
        # return

        return row_data

    except:

        return "Unexpected error: Please reload the page"


########advanced function
@app.route("/Evaluate", methods=["GET"])
def Evaluate():
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

    except:

        return "Article Does Not Exist"


###change
@app.route("/Sources/<articles>", methoda=["GET"])
def sources(articles):
    try:
        # Query
        result = db.engine.execute(
            "SELECT isbn FROM books UNION SELECT articlename FROM externalArticles UNION SELECT articlename FROM scientificpapers;"
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

        return "These Sources cannot be fetched"

