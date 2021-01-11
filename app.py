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

genres = mongo.db.genres


'''
Home page route
'''


@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find().limit(12))
    crime = mongo.db.genres.find_one({"name": "Crime"})
    crimebooks = list(mongo.db.books.find(
        {"genres": ObjectId(crime["_id"])}
    ))
    return render_template(
        "all_books.html",
        books=books,
        crimebooks=crimebooks)


'''
Direct user to login page on function
'''


@app.route("/login_page")
def login_page():
    return render_template("login.html")


'''
Login form route
'''


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


'''
Register form function
'''


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
                "password": generate_password_hash(
                    request.form.get("password")),
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


'''
Log Out button function
'''


@app.route("/logout")
def logout():
    # Remove the user from the session variable and cookies
    session.pop("user")
    return redirect(url_for("login_page"))


'''
Individual book details
'''


@app.route("/get_book/<book_id>")
def get_book(book_id):

    genres = mongo.db.genres.find()

    book_data = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template("book_page.html", book=book_data, genres=genres)


'''
Direct user to add_book.html page
'''


@app.route("/add_book_page")
def add_book_page():
    # Get genres from db
    genres = mongo.db.genres.find().sort("name")
    return render_template("add_book.html", genres=genres)


'''
Add book to database function using a form
'''


@app.route("/add_book", methods=["POST"])
def add_book():

    # Get current users username
    user = mongo.db.users.find_one({"username": session["user"]})

    # Saves image file to mongo db
    if "cover_img" in request.files:
        cover_img = request.files["cover_img"]
        mongo.save_file(cover_img.filename, cover_img)

    # Append genres selected to genre list for book
    genre_list = []
    for genre in request.form.getlist("genre"):
        genre_list.append(ObjectId(genre))

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
            "cover_img_name": cover_img.filename,
            "book_name": request.form.get("book_name"),
            "author": request.form.get("author"),
            "publisher": request.form.get("publisher"),
            "genre": genre_list,
            "pages": request.form.get("pages"),
            "published_date": request.form.get("published_date"),
            "synopsis": request.form.get("synopsis"),
            "isbn": request.form.get("isbn"),
            "user_id": ObjectId(user["_id"]),
            "bookmarked_users": [],
            "reviews": []
        }

        # Inserts book details into database
        mongo.db.books.insert_one(add_book)

        # Find the newest book this user has just added
        new_book = mongo.db.books.find(
            {"user_id": ObjectId(user["_id"])}).sort("_id", -1)

        # Then store the ObjectId in a new variable to get
        # around cursor objects not being able to be updated
        new_book_id = ObjectId(new_book[0]["_id"])

        # Redirects the user to the book page of their newly added book
        return redirect(url_for("get_book", book_id=new_book_id))


'''
Retrieves the uploaded file from user and inserts it into monogdb
'''


@app.route("/get_cover_img/<filename>")
def get_cover_img(filename):
    return mongo.send_file(filename)


'''
Edit a single book route
'''


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):

    genres = mongo.db.genres.find().sort("name")

    # Append genres selected to genre list for book
    genre_list = []
    for genre in request.form.getlist("genre"):
        genre_list.append(ObjectId(genre))

    if request.method == "POST":
        mongo.db.books.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": {
                "book_name": request.form.get("book_name"),
                "author": request.form.get("author"),
                "publisher": request.form.get("publisher"),
                "genre": genre_list,
                "pages": request.form.get("pages"),
                "published_date": request.form.get("published_date"),
                "synopsis": request.form.get("synopsis"),
                "isbn": request.form.get("isbn"),
            }
            }
        )
        return redirect(url_for("get_book", book_id=book_id))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book, genres=genres)


'''
Delete book route
'''


@app.route("/delete_book/<book_id>", methods=["GET", "POST"])
def delete_book(book_id):

    mongo.db.books.remove({"_id": ObjectId(book_id)})

    return redirect(url_for('manage_books', username=session['user']))


'''
Function to display all books that a user has created
'''


@app.route("/manage_books/<username>")
@app.route("/manage_books/<username>/page=<page_num>")
def manage_books(username, page_num=1):
    # Get current users username
    user = mongo.db.users.find_one({"username": username})
    # Find all movies that are added by the user and sort in alphabetical order
    added_books = mongo.db.books.find(
        {"user_id": ObjectId(user["_id"])}).sort("name")

    # How many pages are to be rendered (numbers) used for pagination
    pages = int(added_books.count() / 12) + 1

    # Index the collection of books into sections of 12
    index_start = (int(page_num) - 1) * 12
    index_end = int(page_num) * 12

    return render_template("manage_books.html", user=user,
                           added_books=added_books[index_start:index_end],
                           pages=pages, current_page=int(page_num))


'''
Bookmark a book
'''


@app.route("/bookmark/<book_id>/", methods=["GET", "POST"])
def bookmark(book_id):
    user = mongo.db.users.find_one({"username": session["user"]})

    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$push": {"bookmarked_users": {
            "bookmarked_user_id": ObjectId(user["_id"])
        }}}
    )

    return redirect(url_for("get_book", book_id=book_id))


'''
Remove a book from your bookmarked page
'''


@app.route("/remove_bookmark/<book_id>", methods=["GET", "POST"])
def remove_bookmark(book_id):
    user = mongo.db.users.find_one({"username": session["user"]})

    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$pull": {"bookmarked_users": {
            "bookmarked_user_id": ObjectId(user["_id"])
        }}}
    )

    return redirect(url_for("bookmarked", username=session['user']))


'''
Bookmarked page route
'''


@app.route("/bookmarked/<username>")
@app.route("/bookmarked/<username>/page=<page_num>")
def bookmarked(username, page_num=1):

    # Get current user
    user = mongo.db.users.find_one({"username": username})

    bookmarked_books = mongo.db.books.find(
        {"bookmarked_users": {"bookmarked_user_id": ObjectId(user["_id"])}}
    ).sort("name")

    # How many pages are to be rendered (numbers) used for pagination
    pages = int(bookmarked_books.count() / 12) + 1

    # Index the collection of books into sections of 12
    index_start = (int(page_num) - 1) * 12
    index_end = int(page_num) * 12

    return render_template("bookmarked.html", user=user,
                           bookmarked_books=bookmarked_books[index_start:index_end],
                           pages=pages, current_page=int(page_num))


'''
A single function to redirect user to add_review page when clicked on
corresponding button
'''


@ app.route("/add_review_page/<book_id>")
def add_review_page(book_id):
    book_data = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("add_review.html", book=book_data)


'''
Function to allow user to add a new review for the book they are looking at
'''


@ app.route("/add_review/<book_id>", methods=["POST"])
def add_review(book_id):

    user = mongo.db.users.find_one({"username": session["user"]})
    # $push is used to basically append a new object to the array
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$push": {"reviews": {
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "user": ObjectId(user["_id"]),
        }}}
    )

    return redirect(url_for("get_book", book_id=book_id))


'''
Route to link to exteranl Amazon page
'''


@ app.route("/store_page/<isbn>")
def store_page(isbn):

    amazon_url = "http://www.amazon.co.uk/dp/" + isbn + "/"
    return redirect(amazon_url)


'''
Individual Genre pages
'''


@ app.route("/genre_page/<genre>", methods=["GET", "POST"])
def genre_page(genre):

    selected_genre = mongo.db.genres.find_one({"name": genre})

    genres_books = mongo.db.books.find({"genre": ObjectId(selected_genre._id)})

    return render_template(url_for("genre.html", genres_books=genres_books))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
