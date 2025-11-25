from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/doongool")
def hello_doongool():
    return "<p>Hello, Doongul!</p>"

