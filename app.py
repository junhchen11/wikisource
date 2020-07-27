from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgres://hsejzziyqqzzca:64d03603cdbd5c73eac206ed2a287063278bb6911bb12d9cbf4eb1f1b9481c64@ec2-18-211-48-247.compute-1.amazonaws.com:5432/d6pkpcetbeb8ub"
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/select")
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

    except Exception as e:

        return {"message": dict(e)}, "hello sample"


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


if __name__ == "__main__":
    app.run()
