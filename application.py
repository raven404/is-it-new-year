import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 6 and now.day == 29
    return render_template("index.html", new_year=new_year)
@app.route("/<string:input>")
def data():
    return "Hey Buddy Sorry there is not result for {}!!!".format(name)
