import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("all_books.html", books=books)


@app.route("/get_book/<book_id>")
def get_book(book_id):
    book_data = books.find_one({"_id": ObjectId(book_id)})
    return render_template("book_page.html", book=book_data)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
