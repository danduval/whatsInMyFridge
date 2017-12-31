# SETUP

from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://WhatsInMyFridge:food@localhost:8889/WhatsInMyFridge'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'y337kGcys&zP3B'

db = SQLAlchemy(app)

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    date = db.Column(db.String(50))
    category = db.Column(db.String(50))

    def __init__(self, name, quantity, date, category):
        self.name = name
        self.quantity = quantity
        self.date = date
        self.category = category

# CONTROLLERS

@app.route("/")
def index():
    groceries = Grocery.query.all()

    return render_template("index.html", groceries=groceries)

@app.route("/add", methods=["POST", "GET"])
def add():

    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":

    # get values out of requst object

        name = request.form['name']
        quantity = request.form['quantity']
        date = request.form['date']
        category = request.form['category']

    # create new object with those values

        grocery = Grocery(name, quantity, date, category)

    # add it to the database

        db.session.add(grocery)
        db.session.commit()

        return redirect("/")

# RUN

if __name__ == '__main__':
    app.run()