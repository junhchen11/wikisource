from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgres://hsejzziyqqzzca:64d03603cdbd5c73eac206ed2a287063278bb6911bb12d9cbf4eb1f1b9481c64@ec2-18-211-48-247.compute-1.amazonaws.com:5432/d6pkpcetbeb8ub"

db = SQLAlchemy(app)


@app.route("/select", methods=['GET'])
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

    except:

        return "Select Failed"


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


@app.route("/delArticle/<article>", methods=["GET", "DELETE"])
def delArticle(article):
    try:
        print("hi")
        data = article
        query = "DELETE FROM wikiarticles WHERE name = %s;"
        db.engine.execute(query, data)
        return "deletion successful"
    except:
        return "deletion failed"


@app.route("/insert", methods=["POST"])
def insertArticle():
    try:
        # Query
        req = request.json
        print(req)
        data = (req["url"])
        print(data)
        if data == "https://en.wikipedia.org/wiki/Canada":
            query = "INSERT INTO wikiarticles (url, name) VALUES (%s , 'Canada');"
        elif data == "https://en.wikipedia.org/wiki/Facebook":
            query = "INSERT INTO wikiarticles (url, name) VALUES (%s , 'Facebook');"
        elif data == "https://en.wikipedia.org/wiki/Twitter":
            query = "INSERT INTO wikiarticles (url, name) VALUES (%s , 'Twitter');"
        elif data == "https://en.wikipedia.org/wiki/Artificial Intelligence":
            query = "INSERT INTO wikiarticles (url, name) VALUES (%s , 'Artificial Intelligence');"
        db.engine.execute(query, data)

    except:
        return "insertion Failed"


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
