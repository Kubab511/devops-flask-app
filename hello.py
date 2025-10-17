from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '<p>Welcome, I am a Flask app!</p><a href="/about">About</a><p>   </p><a href="/contact">Contact</a>'

@app.route("/about")
def about():
    return '<p>This is an about page</p><a href="python.org">Python</a><a href="/">Go back</a>'

@app.route("/contact")
def contact():
    return '<p>Contact me at: C23310371@mytudublin.ie</p><a href="/">Go back</a>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
