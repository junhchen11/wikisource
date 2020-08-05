import os
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()
stop_words = nlp.Defaults.stop_words


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
            query = "SELECT url, name FROM wikiarticles WHERE name = %s;"
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
        elif data == "https://en.wikipedia.org/wiki/United_States":
            query = "INSERT INTO wikiarticles (url, name) VALUES (%s , 'United States');"
        db.engine.execute(query, data)
    except:
        return "insertion Failed"


@app.route("/books/<name>", methods=['GET'])
def books(name):
    try:
        # Query
        data = name
        query = "SELECT isbn, title, b.url FROM books b JOIN wikiarticles w ON(b.url = w.url) WHERE name = %s;"
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

        return "Select Failed"


@app.route("/scipapers/<name>", methods=['GET'])
def scipapers(name):
    try:
        # Query
        data = name
        query = "SELECT title, s.url FROM scipapers s JOIN wikiarticles w ON(s.url = w.url) WHERE name = %s"
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

        return "Select Failed"


@app.route("/extarticles/<name>", methods=['GET'])
def extarticles(name):
    try:
        # Query
        data = name
        query = "SELECT articleurl, e.url FROM externalarticles e JOIN wikiarticles w ON (e.url = w.url) WHERE name = %s"
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

        return "Select Failed"


@app.route("/afunction/<aname>/<isbn>", methods=['GET'])
def afunction(aname, isbn):
    try:
        # Query
        data = (isbn, aname)
        print(isbn, aname)
        query = "SELECT b.title FROM books b JOIN wikiarticles w ON (b.url = w.url) WHERE isbn = %s AND w.name = %s;"
        result = db.engine.execute(query, data)
        docCanada = "Canada is a country in the northern part of North America. Its ten provinces and three territories extend from the Atlantic to the Pacific and northward into the Arctic Ocean, covering 9.98 million square kilometres (3.85 million square miles), making it the world's second-largest country by total area. Its southern and western border with the United States, stretching 8,891 kilometres (5,525 mi), is the world's longest bi-national land border. Canada's capital is Ottawa, and its three largest metropolitan areas are Toronto, Montreal, and Vancouver."
        docFacebook = "Facebook(stylized as facebook) is an American online social media and social networking service based in Menlo Park, California and a flagship service of the namesake company Facebook, Inc. It was founded by Mark Zuckerberg, along with fellow Harvard College students and roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz and Chris Hughes.The founders initially limited Facebook membership to Harvard students. Membership was expanded to Columbia, Stanford, and Yale before being expanded to the rest of the Ivy League, MIT, and higher education institutions in the Boston area, then various other universities, and lastly high school students. Since 2006, anyone who claims to be at least 13 years old has been allowed to become a registered user of Facebook, though this may vary depending on local laws. The name comes from the face book directories often given to American university students."
        docArtificialIntelligence = "Artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of intelligent agents: any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[1] Colloquially, the term artificial intelligence is often used to describe machines (or computers) that mimic cognitive functions that humans associate with the human mind, such as learning and problem solving. As machines become increasingly capable, tasks considered to require intelligence are often removed from the definition of AI, a phenomenon known as the AI effect.[3] A quip in Tesler's Theorem says AI is whatever hasn't been done yet.[4] For instance, optical character recognition is frequently excluded from things considered to be AI,[5] having become a routine technology.[6] Modern machine capabilities generally classified as AI include successfully understanding human speech,[7] competing at the highest level in strategic game systems (such as chess and Go),autonomously operating cars, intelligent routing in content delivery networks, and military simulations."
        docTwitter = "Twitter is an American microblogging and social networking service on which users post and interact with messages known as tweets. Registered users can post, like, and retweet tweets, but unregistered users can only read them. Users access Twitter through its website interface, through Short Message Service (SMS) or its mobile-device application software (app).[16] Twitter, Inc. is based in San Francisco, California, and has more than 25 offices around the world.[17] Tweets were originally restricted to 140 characters, but was doubled to 280 for non-CJK languages in November 2017.[18] Audio and video tweets remain limited to 140 seconds for most accounts."
        if result is None:
            return {"message": "Invalid query."}
        rows = result.fetchall()
        # Parse Output
        row_dicts = [dict(row) for row in rows]
        row_data = {"data": row_dicts}
        # return
        titleObject = row_data['data']
        title = titleObject[0]['title']
        if aname == "Canada":
            doc = docCanada
        elif aname == "Facebook":
            doc = docFacebook
        elif aname == "Twitter":
            doc = docTwitter
        elif aname == "Artificial Intelligence":
            doc = docArtificialIntelligence
        print(title)
        print(doc)
        title = nlp(title)
        doc = nlp(doc)
        sum = 0
        count = 0
        for token in title:
            for token1 in doc:
                if token.is_punct is not True:
                    if token not in stop_words and token1 not in stop_words:
                        print(token)
                        print(token1)
                        sim = token1.similarity(token)
                        """ if sim > 0: """
                        sum += sim
                        count += 1

        articleRating = sum/count
        print(articleRating)
        if aname == "Artificial Intelligence":
            articleRating += .10
        if aname == "Facebook":
            articleRating += .08
        if aname == "Twitter":
            articleRating += .06
        return str(articleRating)
    except:
        return "Select Failed"


@app.route("/query1", methods=['GET'])
def query1():
    try:
        # Query

        result = db.engine.execute(
            "SELECT DISTINCT b1.Title, b1.publisher FROM books b1, books b2 WHERE b1.url <> b2.url AND b1.publisher=b2.publisher AND b1.publisher != ')' ORDER BY publisher")
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


@app.route("/query2", methods=['GET'])
def query2():
    try:
        # Query

        result = db.engine.execute(
            "SELECT DISTINCT b1.Title, b1.publisher FROM books b1, books b2 WHERE b1.url <> b2.url AND b1.publisher=b2.publisher AND b1.publisher != ')' ORDER BY publisher")
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


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
