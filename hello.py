from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '<p>Hello, World, I am a Flask app!</p><a href="/about">About</a>'

@app.route("/about")
def about():
    return '<p>This is an about page</p><a href="/">Go back</a>'