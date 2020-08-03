from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from server import app, db


@app.route("/wikiarticles", methods=["GET"])
def wikiarticles():
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
@app.route("/wikiarticles/<article>", methoda=["GET"])
def selectArticle(article):
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

        return "This article does not exist"

