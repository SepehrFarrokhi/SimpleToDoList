from flask import Flask
import database as db

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(error):
    db.close_db(error)


@app.route("/")
def hello_world():
    return db.get_all_tags()


@app.route("/new_tag/<tag_name>")
def new_tag(tag_name):
    print(tag_name)
    db.insert_tags(tag_name)
    return ""






if __name__ == "__main__":
    with app.app_context():
        db.init_db()
    app.run(debug=True)