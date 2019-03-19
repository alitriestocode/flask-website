from flask import Flask
from flask import render_template
from flask import request
import requests
from horoscopeapi import zodiac_sign, get_horoscope

app = Flask("MyApp")

@app.route("/")
def homepage():
    render_template("index.html", message="")

@app.route("/<visitor>")

def hello(visitor):
    return render_template("index.html", message=visitor)

@app.route("/welcome")
def welcome():
    return render_template("index.html", message="Merry Pancake Day to you!")

@app.route("/gen", methods = ["POST"])
def showgeneration():
    form_data = request.form
    year = int(form_data["year"])
    gen = define_gen(year)
    return render_template("gen.html", generation = gen )

#5.Create function to identify which generation user belongs to
# (e.g Gen X 1966 - 1976, Gen Y 1977-1994, Gen Z 1995-2012)
def define_gen(date):
    if date < 1966:
        return "You\'re too old for this function - sorry!"
    if date < 1977:
        return "We think you\'re a valued member of Gen X"
    if date < 1995:
        return "You\'re probably a member of Gen Y"
    if date < 2013:
        return "You are 100% Gen Z"
    else:
        return "Can you even type yet? You're too young, go play outside."
@app.route("/horoscope", methods = ["POST"])
def showhoroscope():
    form_data = request.form
    month = int(form_data["month"])
    day = int(form_data["day"])
    z_sign = zodiac_sign(month, day)
    data = get_horoscope(z_sign)
    print "Month is "+ str(month)
    print "Day is "+ str(day)
    print z_sign
    return render_template("horoscope.html", data = data)


app.run(debug=True)
