import time, redis, json
from flask import Flask

r = redis.Redis(host='redis-server', port=6379, decode_responses=True)
app = Flask(__name__)

@app.route("/")
def hello():
    data = r.get('hello')
    if data is not None and isinstance(data, str):
        data = json.loads(data)
        if time.time() - data['time'] <= 600:
            return data['html']
    data = '<p>Welcome, I am a Flask app!</p><a href="/about">About</a><p>   </p><a href="/contact">Contact</a>'
    r.set('hello', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data

@app.route("/about")
def about():
    data = r.get('about')
    if data is not None and isinstance(data, str):
        data = json.loads(data)
        if time.time() - data['time'] <= 600:
            return data['html']
    data = '<p>This is an about page</p><a href="python.org">Python</a><a href="/">Go back</a>'
    r.set('about', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data

@app.route("/contact")
def contact():
    data = r.get('contact')
    if data is not None and isinstance(data, str):
        data = json.loads(data)
        if time.time() - data['time'] <= 600:
            return data['html']
    data = '<p>Contact me at: C23310371@mytudublin.ie</p><a href="/">Go back</a>'
    r.set('contact', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
