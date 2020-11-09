import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import os


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World ... again for the second time ... testing 1 . 2 . 3"
