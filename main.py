from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/users', methods=['GET'])
def get_all_users():
    return {0: "Khanh", 1: "Chan"}


@app.route('/api/users/<string:name>', methods=['GET'])
def get_users(name):
    return name


@app.route('/api/<string:name>', methods=['GET'])
def get_name(name):
    return jsonify(name=name)
    return jsonify({"name": name})


@app.route('/api/<string:name>/item', methods=['GET'])
def get_name_item(name):
    return name


@app.route('/api/abc', methods=['POST'])
def post_abc():
    abc = request.get_json()
    return jsonify(abc=abc)


users = [{"id": 1, "name": "Khanh"}, {"id": 2, "name": "Chan"}, {"id": 3, "name": "Sy"}]


@app.route('/api/user/<string:id>')
def get_user(id):
    id=int(id)
    for item in users:
        if item["id"] == id:
            return jsonify(item)
    return jsonify(message="Ko co")


app.run(port=5000)
