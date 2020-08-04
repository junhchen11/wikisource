from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


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


# change
@app.route("/wikiarticles/<article>", methods=["GET", "DELETE"])
def selectArticle(article):
    if request.method == "GET":
        try:
            data = article
            query = "SELECT url FROM wikiarticles WHERE name = %s;"
            # Query

            result = db.engine.execute(query, data)
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
    elif request.method == "DELETE":
        try:
            data = article
            query = "DELETE FROM wikiarticles WHERE name = %s"
            db.engine.execute(query, data)
            return "deletion successful"
        except:
            return "deletion failed"
