from flask import Flask
from flask import render_template
from flask import request
import requests 
app = Flask("MyApp")

@app.route("/<visitor>")

def hello(visitor):
    return render_template("index.html", message=visitor)

@app.route("/")
def homepage():
    return "Type your name in the URL!"

@app.route("/welcome")
def welcome():
    return "Merry Pancake Day to you!"



app.run(debug=True)
