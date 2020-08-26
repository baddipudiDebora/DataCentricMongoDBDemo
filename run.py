import json
import os  
from flask import Flask, render_template, url_for, request, session, redirect
from datetime import datetime
from flask import Flask, json, redirect, render_template, request, session, url_for, flash, g
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import bcrypt

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:RootUser@myfirstcluster.zhfps.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html", page_title="Shop Online")


@app.route('/about')
def about():
    return render_template("about-us.html", page_title="Shop Online")


@app.route('/contact')
def contact():
    return render_template("contact-us.html", page_title="Shop Online")


@app.route('/login')
def login():
    return render_template("login.html", page_title="Shop Online")


@app.route('/register')
def register():
    return render_template("register.html", page_title="register")


@app.route('/addlisting')
def addlisting():
    return render_template("ad-listing.html", page_title="Add Listing")


@app.route('/viewlisting')
def viewlisting():
    return render_template("ad-listing.html", page_title="View Listing")


@app.route('/userprofile')
def userprofile():
    return render_template("user-profile.html", page_title="Shop Online")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

