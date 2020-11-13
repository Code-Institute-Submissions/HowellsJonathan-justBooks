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


@app.route("/login_page")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if a username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check if the hashed password mathes input from user
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("get_books"))
            else:
                # Flash is password is wrong
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username isn't in the database
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if a username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username Taken")
            return redirect(url_for("register"))
        elif (existing_user is None):
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password")),
                "bookmarked": [],
                "my_reviews": [],
                "my_books": [],
            }
            # Inserts registration data to the database
            mongo.db.users.insert_one(register)
            # Put the user into session variable to pull on other pages
            session["user"] = request.form.get("username").lower()
            return redirect(url_for("get_books"))

    return render_template("register.html")


@app.route("/get_book/<book_id>")
def get_book(book_id):
    book_data = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("book_page.html", book=book_data)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
