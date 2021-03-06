import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import TEXT
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/front_page")
@app.route("/")
def front_page():
    '''
    Home page route
    '''
    books = list(mongo.db.books.find().limit(12))
    genres = list(mongo.db.genres.find().sort("name"))
    return render_template(
        "front_page.html",
        books=books,
        genres=genres)


@app.route("/login_page")
def login_page():
    '''
    Direct user to login page on function
    '''
    genres = list(mongo.db.genres.find().sort("name"))
    return render_template("login.html", genres=genres)


@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    Login form route
    '''
    if request.method == "POST":
        # Check if a username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # Check if the hashed password mathes input from user
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Logged In Successfully")
                return redirect(url_for("front_page"))
            else:
                # Flash is password is wrong
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login_page"))
        else:
            # Username isn't in the database
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login_page"))


@app.route("/register", methods=["GET", "POST"])
def register():
    '''
    Register form function
    '''
    genres = list(mongo.db.genres.find().sort("name"))
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
            }
            # Inserts registration data to the database
            mongo.db.users.insert_one(register)
            # Put the user into session variable to pull on other pages
            session["user"] = request.form.get("username").lower()
            flash("Registered Successfully")
            return redirect(url_for("front_page"))

    return render_template("register.html", genres=genres)


@app.route("/logout")
def logout():
    '''
    Log Out button function
    '''
    # Remove the user from the session variable and cookies
    flash("Logged Out Successfully")
    session.pop("user")
    return redirect(url_for("login_page"))


@app.route("/get_book/<book_id>")
def get_book(book_id):
    '''
    Individual book details
    '''
    genres = list(mongo.db.genres.find().sort("name"))
    book_data = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("book_page.html", book=book_data, genres=genres)


@app.route("/add_book_page")
def add_book_page():
    '''
    Direct user to add_book.html page
    '''
    # Get genres from db
    genres = list(mongo.db.genres.find().sort("name"))
    return render_template("add_book.html", genres=genres)


@app.route("/add_book", methods=["POST"])
def add_book():
    '''
    Add book to database function using a form
    '''
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
        flash("Added Book Successfully")
        # Redirects the user to the book page of their newly added book
        return redirect(url_for("get_book", book_id=new_book_id))


@app.route("/get_cover_img/<filename>")
def get_cover_img(filename):
    '''
    Retrieves the uploaded file from user and inserts it into monogdb
    '''
    return mongo.send_file(filename)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    '''
    Edit a single book route
    '''
    genres = list(mongo.db.genres.find().sort("name"))
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
        flash("Updated Book")
        return redirect(url_for("get_book", book_id=book_id))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book, genres=genres)


@app.route("/delete_book/<book_id>", methods=["GET", "POST"])
def delete_book(book_id):
    '''
    Delete book route
    '''
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Deleted")
    return redirect(url_for('manage_books', username=session['user']))


@app.route("/manage_books/<username>")
@app.route("/manage_books/<username>/page=<page_num>")
def manage_books(username, page_num=1):
    '''
    Function to display all books that a user has created
    '''
    genres = list(mongo.db.genres.find().sort("name"))
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
                           pages=pages,
                           current_page=int(page_num),
                           genres=genres)


@app.route("/bookmark/<book_id>/", methods=["GET", "POST"])
def bookmark(book_id):
    '''
    Bookmark a book
    '''
    user = mongo.db.users.find_one({"username": session["user"]})
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$push": {"bookmarked_users": {
            "bookmarked_user_id": ObjectId(user["_id"])
        }}}
    )
    flash("Bookmarked")
    return redirect(url_for("get_book", book_id=book_id))


@app.route("/remove_bookmark/<book_id>", methods=["GET", "POST"])
def remove_bookmark(book_id):
    '''
    Remove a book from your bookmarked page
    '''
    user = mongo.db.users.find_one({"username": session["user"]})
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$pull": {"bookmarked_users": {
            "bookmarked_user_id": ObjectId(user["_id"])
        }}}
    )
    flash("Bookmark Removed")
    return redirect(url_for("bookmarked", username=session['user']))


@app.route("/bookmarked/<username>")
@app.route("/bookmarked/<username>/page=<page_num>")
def bookmarked(username, page_num=1):
    '''
    Bookmarked page route
    '''
    genres = list(mongo.db.genres.find().sort("name"))
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
                           pages=pages, current_page=int(page_num), genres=genres)


@ app.route("/add_review_page/<book_id>")
def add_review_page(book_id):
    '''
    A single function to redirect user to add_review page when clicked on
    corresponding button
    '''
    book_data = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("add_review.html", book=book_data)


@ app.route("/add_review/<book_id>", methods=["POST"])
def add_review(book_id):
    '''
    Function to allow user to add a new review for the book they are looking at
    '''
    user = mongo.db.users.find_one({"username": session["user"]})
    # $push is used to basically append a new object to the array
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$push": {"reviews": {
            "review_id": ObjectId(),
            "review_title": request.form.get("review_title"),
            "review": request.form.get("review"),
            "user_handle": user["username"]
        }}}
    )
    flash("Review Added")
    return redirect(url_for("get_book", book_id=book_id))


@app.route("/edit_review/<review_id>/<book_id>", methods=["GET", "POST"])
def edit_review(review_id, book_id):
    '''
    Edit Review
    '''
    if request.method == "POST":
        mongo.db.books.update_one(
            # As I am only updating one particluar element of an
            # array I have to call two _id's or query parameters
            # by seperating them with a comma
            {"_id": ObjectId(book_id),
             "reviews.review_id": ObjectId(review_id)},
            {"$set": {"reviews.$.review": request.form.get("review"),
                      "reviews.$.review_title": request.form.get("review_title")}}
        )
        flash("Review Edited")
        return redirect(url_for("get_book", book_id=book_id))
    # To get just the ID and the correct review I first
    # find the correct book then match the review_id
    # using $elemMatch to the review_id
    # This outputs to console book_id and review data
    selected_review = list(mongo.db.books.find(
        {"_id": ObjectId(book_id)},
        {"reviews": {"$elemMatch": {
            "review_id": ObjectId(review_id)
        }}}
    ))
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template(
        "edit_review.html",
        selected_review=selected_review,
        book=book,
        review_id=review_id)


@app.route("/delete_review/<book_id>/<review_id>")
def delete_review(book_id, review_id):
    '''
    Delete Review
    '''
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$pull": {"reviews":
                   {"review_id": ObjectId(review_id)}}}
    )
    flash("Review Deleted")
    return redirect(url_for("get_book", book_id=book_id))


@ app.route("/store_page/<isbn>")
def store_page(isbn):
    '''
    Route to link to exteranl Amazon page
    '''
    amazon_url = "http://www.amazon.co.uk/dp/" + isbn + "/"
    return redirect(amazon_url)


@ app.route("/genre_page/<genre>")
@ app.route("/genre_page/<genre>/page=<page_num>")
def genre_page(genre, page_num=1):
    '''
    Individual Genre pages
    '''
    genres = list(mongo.db.genres.find().sort("name"))
    genre_doc = mongo.db.genres.find_one({"_id": ObjectId(genre)})
    genres_books = list(mongo.db.books.find({"genre": ObjectId(genre)}))
    count_of_books = int(mongo.db.books.count_documents(
        {"genre": ObjectId(genre)}))
    # How many pages are to be rendered (numbers) used for pagination
    pages = int(mongo.db.books.count_documents(
        {"genre": ObjectId(genre)}) / 12) + 1
    # Index the collection of books into sections of 12
    index_start = (int(page_num) - 1) * 12
    index_end = int(page_num) * 12
    return render_template("genre.html",
                           books=genres_books[index_start:index_end],
                           pages=pages,
                           current_page=int(page_num),
                           count=count_of_books,
                           genre_doc=genre_doc,
                           genres=genres)


@ app.route("/search", methods=["POST"])
@ app.route("/search/page=<page_num>")
def search(page_num=1):
    '''
    Search bar
    '''
    # Search and text function is allowed due to having made an index
    # in mongodb for certain keys
    result = list(mongo.db.books.find(
        {"$text": {"$search": request.form.get("user-search")}}))
    # A list cannot be counted so I have to count a cursor
    # from mpymongo instead
    result_for_count = mongo.db.books.find(
        {"$text": {"$search": request.form.get("user-search")}})
    count = int(result_for_count.count())
    # How many pages are to be rendered (numbers) used for pagination
    pages = int(count / 12) + 1

    print(pages)
    # Index the collection of books into sections of 12
    index_start = (int(page_num) - 1) * 12
    index_end = int(page_num) * 12
    # Find genres for genre dropdown
    genres = list(mongo.db.genres.find().sort("name"))
    return render_template("search.html",
                           result=result[index_start:index_end],
                           genres=genres,
                           count=count,
                           pages=pages,
                           current_page=int(page_num))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
