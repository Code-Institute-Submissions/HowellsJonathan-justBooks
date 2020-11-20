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

# Home Page Function


@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("all_books.html", books=books)

# Direct user to login page on function


@app.route("/login_page")
def login_page():
    return render_template("login.html")

# Login form function


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
                return redirect(url_for("login_page"))

        else:
            # Username isn't in the database
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login_page"))

# Register form function


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if a username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        # If username already exists alert user they need to pick a new one
        if existing_user:
            flash("Username Taken")
            return redirect(url_for("register"))
        else:
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

# Log Out button function


@app.route("/logout")
def logout():
    # Remove the user from the session variable and cookies
    session.pop("user")
    return redirect(url_for("login_page"))


# Individual book details
@app.route("/get_book/<book_id>")
def get_book(book_id):
    book_data = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("book_page.html", book=book_data)


# Direct user to add_book.html page
@app.route("/add_book_page")
def add_book_page():
    return render_template("add_book.html")


# Add book to database function using a form
@app.route("/add_book", methods=["POST"])
def add_book():

    # Get current users username
    user = mongo.db.users.find_one({"username": session["user"]})

    # Check is ISBN or Name already exists in database
    existing_isbn = mongo.db.books.find_one(
        {"isbn": request.form.get("isbn").lower()}
    )
    # If ISBN exists do not let user add the same book
    if existing_isbn:
        flash("Book Already Exists")
        return redirect(url_for("add_book"))
    else:
        # Adding book to the database using requests from the form
        add_book = {
            "book_name": request.form.get("book_name"),
            "author": request.form.get("author"),
            "publisher": request.form.get("publisher"),
            "genre": request.form.get("genre"),
            "pages": request.form.get("pages"),
            "published_date": request.form.get("published_date"),
            "synopsis": request.form.get("synopsis"),
            "isbn": request.form.get("isbn"),
            "user_id": ObjectId(user["_id"]),
            "reviews": [],
        }

        # Inserts book details into database
        mongo.db.books.insert_one(add_book)

        # Find the newest book this user has just added
        new_book = mongo.db.books.find(
            {"user_id": ObjectId(user["_id"])}).sort("_id", -1)

        # Then store the ObjectId in a new variable to get
        # around cursor objects not being able to be updated
        new_book_id = ObjectId(new_book[0]["_id"])

        # Push the new _id into the array my_books for session user
        mongo.db.users.update_one(
            {"username": user["username"]},
            {"$push": {"my_books": {
                "book_id": new_book_id,
            }}}
        )

        # Redirects the user to the book page of their newly added book
        return redirect(url_for("get_book", book_id=new_book_id))


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        edit = {
            "book_name": request.form.get("book_name"),
            "author": request.form.get("author"),
            "publisher": request.form.get("publisher"),
            "genre": request.form.get("genre"),
            "pages": request.form.get("pages"),
            "published_date": request.form.get("published_date"),
            "synopsis": request.form.get("synopsis"),
            "isbn": request.form.get("isbn"),
            "user_id": ObjectId(user["_id"]),
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, edit)

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_task.html", book=book)


@app.route("/manage_books/<username>")
def manage_books(username):
    # Get current users username
    user = mongo.db.users.find_one({"username": username})
    # Find all movies that are added by the user
    added_books = mongo.db.books.find(
        {"user_id": ObjectId(user["_id"])})

    return render_template("manage_books.html", user=user, added_books=added_books)


# A single function to redirect user to add_review page when clicked on
# corresponding button
@app.route("/add_review_page/<book_id>")
def add_review_page(book_id):
    book_data = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("add_review.html", book=book_data)


# Functino to allow user to add a new review for the book they are looking at
@app.route("/add_review/<book_id>", methods=["POST"])
def add_review(book_id):
    # $push is used to basically append a new object to the array
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$push": {"reviews": {
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "user": session["user"],
        }}}
    )

    return redirect(url_for("get_book", book_id=book_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
