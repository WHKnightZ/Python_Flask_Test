from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
from flask_jwt import jwt_required, JWT

# from security import authenticate, identity
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

class DevConfig:
    ENV = 'development'
    DEBUG = True
    DEBUG_TB_ENABLED = True  # Disable Debug toolbar
    HOST = '0.0.0.0'
    TEMPLATES_AUTO_RELOAD = True
    # JWT Config
    JWT_SECRET_KEY = '1234567a@'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    # msql
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SCHEDULER_API_ENABLED = False


app = Flask(__name__)
app.config.from_object(DevConfig)
api = Api(app)

# jwt = JWT(app, authenticate, identity)

items = []

db = SQLAlchemy(app)
ma = Marshmallow()
db.init_app(app)
ma.init_app(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    @staticmethod
    def get_all():
        return User.query.order_by(User.username).all()

    @staticmethod
    def get_by_id(_id):
        return User.query.get(_id)


class Item(Resource):
    # @app.route('/item/<string:name>')
    # @jwt_required()
    def get(self, name):
        item = User.get_all()
        print(len(item))
        z = []
        for i in item:
            z.append({"username": i.username, "password": i.password})
        # item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': z}, 200 if item else 404

    # @jwt_required()
    def post(self, name):
        data = request.get_json()
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {"message": f"an item with name {name} is already exists"}, 400
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    # @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] == name, items))
        return {"message": 'Item deleted'}

    # @jwt_required()
    def put(self, name):
        data = request.get_json()
        global items
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            item.update(data)
        else:
            item = {"name": name, "price": data["price"]}
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
