from flask import Flask, jsonify, request, render_template

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    # @app.route('/item/<string:name>')
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        data = request.get_json()
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {"message": f"an item with name {name} is already exists"}, 400
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000)

# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# @app.route('/api/users', methods=['GET'])
# def get_all_users():
#     return {0: "Khanh", 1: "Chan"}
#
#
#
# @app.route('/api/users/<string:name>', methods=['GET'])
# def get_users(name):
#     return name
#
#
# @app.route('/api/<string:name>', methods=['GET'])
# def get_name(name):
#     return jsonify(name=name)
#     return jsonify({"name": name})
#
#
# @app.route('/api/<string:name>/item', methods=['GET'])
# def get_name_item(name):
#     return name
#
#
# @app.route('/api/abc', methods=['POST'])
# def post_abc():
#     abc = request.get_json()
#     return jsonify(abc=abc)
#
#
# users = [{"id": 1, "name": "Khanh"}, {"id": 2, "name": "Chan"}, {"id": 3, "name": "Sy"}]
#
#
# @app.route('/api/user/<string:id>')
# def get_user(id):
#     id=int(id)
#     for item in users:
#         if item["id"] == id:
#             return jsonify(item)
#     return jsonify(message="Ko co")
#
#
# app.run(port=5000)
