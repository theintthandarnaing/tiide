from flask import Flask

app = Flask(__name__)

@app.route("/")
def theint():
    return "Hello World"

@app.route("/theint")
def tiide():
    return "Welcome to Theint"
