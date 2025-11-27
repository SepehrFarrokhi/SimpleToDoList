from flask import Flask, jsonify, request
import database as db

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(error):
    db.close_db(error)


@app.route("/")
def index():
    return db.get_all_tags()


@app.route("/tags", methods=["GET"])
def get_tags():
    rows = db.get_all_tags()
    tags = [dict(r) for r in rows]
    return jsonify(tags)



@app.route("/tags", methods = ["PUT"])
def put_tags():
    data = request.get_json()
    if not data or "tag_name" not in data:
        return jsonify({"error": "Value Missing 'tag_name' error"}), 400  
    tname = data.get("tag_name")
    res = db.insert_tags(tname) 
    return jsonify(dict(res)), 200 



@app.route("/new_tag/<tag_name>")
def new_tag(tag_name):
    print(tag_name)
    db.insert_tags(tag_name)
    return ""






if __name__ == "__main__":
    with app.app_context():
        db.init_db()
    app.run(debug=True)