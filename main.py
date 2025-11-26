from flask import Flask
import database as db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    with app.app_context():
        db.init_db()
    app.run(debug=True)


